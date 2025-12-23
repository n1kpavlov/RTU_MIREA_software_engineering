import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def generate_attraction_points(n, width, height):
    return np.random.rand(n, 2) * [width, height]

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

def grow_tree(nodes, segments, nearest_nodes, D):
    new_nodes = []
    for v_index, points in nearest_nodes.items():
        v = nodes[v_index]
        direction = np.sum([(point - v) / np.linalg.norm(point - v) for point in points], axis=0)
        if np.linalg.norm(direction) == 0:
            continue

        direction_normalized = direction / np.linalg.norm(direction)
        v_new = v + direction_normalized * D

        new_nodes.append(v_new)
        segments.append((v, v_new))
    return new_nodes

def space_colonization(width, height, n_attraction_points, di, dk, D, max_steps):
    attraction_points = generate_attraction_points(n_attraction_points, width, height)
    # Начальный узел один - в центре нижней границы
    nodes = [np.array([width / 2, 10])]
    segments = []

    for step in range(max_steps):
        nearest_nodes = find_nearest_nodes(attraction_points, np.array(nodes), di)
        if not nearest_nodes:
            break

        new_nodes = grow_tree(nodes, segments, nearest_nodes, D)
        nodes.extend(new_nodes)

        # Удаление поглощенных точек
        to_remove = []
        for point in attraction_points:
            distances = np.linalg.norm(nodes - point, axis=1)
            if np.min(distances) < dk:
                to_remove.append(point)
        attraction_points = np.array([point for point in attraction_points if not any(np.array_equal(point, p) for p in to_remove)])

    return nodes, segments

def plot_tree(nodes, segments, width, height):
    fig, ax = plt.subplots()
    lc = LineCollection(segments, colors='green', linewidths=2)
    ax.add_collection(lc)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    plt.show()

# Параметры
width, height = 800, 800
n_attraction_points = 500
di = 100
dk = 20
D = 10
max_steps = 1000

# Генерация и отображение одного дерева
nodes, segments = space_colonization(width, height, n_attraction_points, di, dk, D, max_steps)
plot_tree(nodes, segments, width, height)