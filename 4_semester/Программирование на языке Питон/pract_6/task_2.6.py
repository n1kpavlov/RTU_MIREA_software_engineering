import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def generate_attraction_points(n, width, height, trunk_height):
    points = np.random.rand(n, 2) * [width, height]
    # Фильтруем точки только выше ствола
    return points[points[:, 1] > trunk_height]


def find_nearest_nodes(attraction_points, nodes, di):
    nearest_nodes = {}
    for point in attraction_points:
        distances = np.linalg.norm(nodes - point, axis=1)
        nearest_index = np.argmin(distances)
        if distances[nearest_index] < di:
            if nearest_index in nearest_nodes:
                nearest_nodes[nearest_index].append(point)
            else:
                nearest_nodes[nearest_index] = [point]
    return nearest_nodes


def grow_tree(nodes, segments, nearest_nodes, D, trunk_height):
    new_nodes = []
    for v_index, points in nearest_nodes.items():
        v = nodes[v_index]
        direction = np.sum([(point - v) / np.linalg.norm(point - v) for point in points], axis=0)
        if np.linalg.norm(direction) == 0:
            continue

        direction_normalized = direction / np.linalg.norm(direction)
        v_new = v + direction_normalized * D

        # Добавляем только ветки выше ствола
        if v_new[1] >= trunk_height:
            new_nodes.append(v_new)
            segments.append((v, v_new))

    return new_nodes


def space_colonization(width, height, n_attraction_points, di, dk, D, max_steps, trunk_height):
    # Генерируем ствол
    trunk_base = np.array([width / 2, 10])
    nodes = [trunk_base]
    segments = []

    # Строим вертикальный ствол
    trunk_top = np.array([width / 2, trunk_height])
    nodes.append(trunk_top)
    segments.append((trunk_base, trunk_top))

    # Генерируем точки притяжения выше ствола
    attraction_points = generate_attraction_points(n_attraction_points, width, height, trunk_height)
    leaves = []

    # Основной цикл роста
    for _ in range(max_steps):
        nearest_nodes = find_nearest_nodes(attraction_points, np.array(nodes), di)
        if not nearest_nodes:
            break

        new_nodes = grow_tree(nodes, segments, nearest_nodes, D, trunk_height)
        nodes.extend(new_nodes)

        # Собираем поглощенные точки как листья
        to_remove = []
        for point in attraction_points:
            distances = np.linalg.norm(nodes - point, axis=1)
            if np.min(distances) < dk:
                to_remove.append(point)
        attraction_points = np.array([p for p in attraction_points if not any(np.array_equal(p, t) for t in to_remove)])
        leaves.extend(to_remove)

    return nodes, segments, leaves


def plot_tree(nodes, segments, leaves, width, height):
    fig, ax = plt.subplots(figsize=(10, 10))

    # Рисуем ствол и ветки
    lc = LineCollection(segments, colors='#4a3728', linewidths=3, zorder=2)
    ax.add_collection(lc)

    # Рисуем листья увеличенного размера
    if len(leaves) > 0:
        leaves = np.array(leaves)
        ax.scatter(
            leaves[:, 0], leaves[:, 1],
            c='green',
            s=600,
            alpha=0.6,
            zorder=3,
            marker='o',
            edgecolors='none'
        )

    # Настройки отображения
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    #ax.axis('off')
    plt.show()


# Параметры генерации
width, height = 300, 400
n_attraction_points = 400
di = 70  # Радиус влияния
dk = 12  # Радиус поглощения
D = 15  # Длина шага роста
max_steps = 250
trunk_height = 150  # Высота ствола

# Генерация и отрисовка
nodes, segments, leaves = space_colonization(
    width, height, n_attraction_points, di, dk, D, max_steps, trunk_height
)
plot_tree(nodes, segments, leaves, width, height)