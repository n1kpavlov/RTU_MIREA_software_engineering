import numpy as np
import matplotlib.pyplot as plt
import random


PICO8_PALETTE = [
    (29, 43, 83),   # 1D2B53
    (126, 37, 83),  # 7E2553
    (0, 135, 81),   # 008751
    (171, 82, 54),  # AB5236
    (95, 87, 79),   # 5F574F
    (194, 195, 199),# C2C3C7
    (255, 241, 232),# FFF1E8
    (255, 0, 77),   # FF004D
    (255, 163, 0),  # FFA300
    (255, 236, 39), # FFEC27
    (0, 228, 54),   # 00E436
    (41, 173, 255), # 29ADFF
    (131, 118, 156),# 83769C
    (255, 119, 168),# FF77A8
    (255, 204, 170) # FFCCAA
]


def generate_symmetric_sprite(sprite_height, sprite_width):
    sprite = np.zeros((sprite_height, sprite_width, 3), dtype=int)
    palette = [0, 0, random.choice(PICO8_PALETTE), random.choice(PICO8_PALETTE)]

    for i in range(sprite_height):
        for j in range((sprite_width + 1) // 2):
            sprite[i, j] = random.choice(palette)

    for i in range(sprite_height):
        for j in range((sprite_width + 1) // 2, sprite_width):
            sprite[i, j] = sprite[i, sprite_width - 1 - j]

    return sprite


def generate_sprite_map(rows, cols, sprite_height, sprite_width, padding):
    map_height = rows * sprite_height + (rows + 1) * padding
    map_width = cols * sprite_width + (cols + 1) * padding

    sprite_map = np.zeros((map_height, map_width, 3), dtype=int)

    for i in range(rows):
        for j in range(cols):
            sprite = generate_symmetric_sprite(sprite_height, sprite_width)
            start_row = i * (sprite_height + padding) + padding
            start_col = j * (sprite_width + padding) + padding
            sprite_map[start_row:start_row + sprite_height, start_col:start_col + sprite_width] = sprite

    return sprite_map


def display_sprite_map(sprite_map):
    plt.imshow(sprite_map)
    plt.axis('off')
    plt.show()


rows = 10
cols = 20
sprite_height = 8
sprite_width = 7
padding = 4

sprite_map = generate_sprite_map(rows, cols, sprite_height, sprite_width, padding)
display_sprite_map(sprite_map)