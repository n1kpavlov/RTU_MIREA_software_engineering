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

def display_sprite(sprite):
    plt.imshow(sprite, cmap='gray')
    plt.axis('off')
    plt.show()

sprite = generate_symmetric_sprite(5)
display_sprite(sprite)