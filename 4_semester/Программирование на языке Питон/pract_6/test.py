import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def generate_attraction_points(n, width, height, crown_center, crown_radius):
    points = []
    while len(points) < n:
        x = np.random.uniform(crown_center[0] - crown_radius,
                              crown_center[0] + crown_radius)
        y = np.random.uniform(crown_center[1] - crown_radius,
                              crown_center[1] + crown_radius)
        if np.linalg.norm([x - crown_center[0], y - crown_center[1]]) <= crown_radius:
            points.append([x, y])
    return np.array(points)


def find_nearest_nodes(attraction_points, nodes, influence_radius):
    nearest_nodes = {}
    for point in attraction_points:
        distances = np.linalg.norm(nodes - point, axis=1)
        nearest_index = np.argmin(distances)
        if distances[nearest_index] < influence_radius:
            if nearest_index in nearest_nodes:
                nearest_nodes[nearest_index].append(point)
            else:
                nearest_nodes[nearest_index] = [point]
    return nearest_nodes


def grow_tree(nodes, segments, nearest_nodes, step_size, thickness):
    new_nodes = []
    for v_index, points in nearest_nodes.items():
        v = nodes[v_index]
        direction = np.sum([(point - v) / np.linalg.norm(point - v) for point in points], axis=0)
        if np.linalg.norm(direction) == 0:
            continue

        direction_normalized = direction / np.linalg.norm(direction)
        v_new = v + direction_normalized * step_size

        # Наследование толщины и уменьшение для новых веток
        new_thickness = max(thickness[v_index] * 0.7, 0.5)
        thickness.append(new_thickness)

        new_nodes.append(v_new)
        segments.append((v, v_new, new_thickness))
    return new_nodes


def generate_tree(width=800,
                  height=800,
                  trunk_height=300,
                  crown_radius=200,
                  attraction_points_count=300,
                  influence_radius=80,
                  kill_radius=15,
                  step_size=20,
                  max_iterations=200):
    # Инициализация ствола
    trunk_base = np.array([width / 2, 10])
    trunk_top = np.array([width / 2, trunk_height])

    nodes = [trunk_base, trunk_top]
    segments = [(trunk_base, trunk_top, 10)]  # Начальная толщина ствола
    thickness = [10, 8]  # Толщина для узлов

    # Генерация точек притяжения в кроне
    crown_center = np.array([width / 2, trunk_height + crown_radius / 2])
    attraction_points = generate_attraction_points(
        attraction_points_count,
        width,
        height,
        crown_center,
        crown_radius
    )

    leaves = []

    # Процесс роста дерева
    for _ in range(max_iterations):
        nearest_nodes = find_nearest_nodes(attraction_points, np.array(nodes), influence_radius)
        if not nearest_nodes:
            break

        new_nodes = grow_tree(nodes, segments, nearest_nodes, step_size, thickness)
        nodes.extend(new_nodes)

        # Сбор листьев
        new_leaves = [nodes[i] for i in nearest_nodes.keys()]
        leaves.extend(new_leaves)

        # Удаление поглощенных точек
        to_remove = []
        for point in attraction_points:
            distances = np.linalg.norm(nodes - point, axis=1)
            if np.min(distances) < kill_radius:
                to_remove.append(point)
        attraction_points = np.array([p for p in attraction_points if not any(np.all(p == t) for t in to_remove)])

    return segments, leaves, crown_center


def plot_tree(segments, leaves, crown_center):
    fig, ax = plt.subplots(figsize=(10, 10))

    # Отрисовка ветвей с разной толщиной
    lines = []
    widths = []
    for seg in segments:
        lines.append([seg[0], seg[1]])
        widths.append(seg[2])

    lc = LineCollection(lines, linewidths=widths, colors='#5d3f1d', zorder=2)
    ax.add_collection(lc)

    # Отрисовка листьев
    if leaves:
        leaves = np.array(leaves)
        ax.scatter(leaves[:, 0], leaves[:, 1], c='#2d5a27', s=50,
                   alpha=0.7, zorder=3, marker='8')

    # Отрисовка кроны
    crown = plt.Circle(crown_center, crown_radius * 1.2, color='#2d5a2755', zorder=1)
    ax.add_patch(crown)

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()


# Параметры дерева
width, height = 800, 800
trunk_height = 250
crown_radius = 180
attraction_points_count = 400
influence_radius = 70
kill_radius = 12
step_size = 18
max_iterations = 250

# Генерация и отрисовка дерева
segments, leaves, crown_center = generate_tree(
    width=width,
    height=height,
    trunk_height=trunk_height,
    crown_radius=crown_radius,
    attraction_points_count=attraction_points_count,
    influence_radius=influence_radius,
    kill_radius=kill_radius,
    step_size=step_size,
    max_iterations=max_iterations
)

plot_tree(segments, leaves, crown_center)