import numpy as np
import matplotlib.pyplot as plt


def generate_symmetric_sprite(size):
    sprite = np.zeros((size, size), dtype=int)

    for i in range(size):
        for j in range((size + 1) // 2):
            sprite[i, j] = np.random.randint(0, 2)

    for i in range(size):
        for j in range((size + 1) // 2, size):
            sprite[i, j] = sprite[i, size - 1 - j]

    return sprite


def generate_sprite_map(rows, cols, sprite_size, padding):
    map_height = rows * sprite_size + (rows + 1) * padding
    map_width = cols * sprite_size + (cols + 1) * padding

    sprite_map = np.zeros((map_height, map_width), dtype=int)

    for i in range(rows):
        for j in range(cols):
            sprite = generate_symmetric_sprite(sprite_size)
            start_row = i * (sprite_size + padding) + padding
            start_col = j * (sprite_size + padding) + padding
            sprite_map[start_row:start_row + sprite_size, start_col:start_col + sprite_size] = sprite

    return sprite_map


def display_sprite_map(sprite_map):
    plt.imshow(sprite_map, cmap='gray')
    plt.axis('off')
    plt.show()


rows = 10
cols = 20
sprite_size = 5
padding = 4

sprite_map = generate_sprite_map(rows, cols, sprite_size, padding)
display_sprite_map(sprite_map)