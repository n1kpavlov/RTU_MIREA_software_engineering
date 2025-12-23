import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def noise(x, y):
    return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1


def val_noise(x, y):
    x0 = int(x)
    y0 = int(y)
    x1 = x0 + 1
    y1 = y0 + 1

    s = x - x0
    t = y - y0

    s = s * s * (3.0 - 2.0 * s)
    t = t * t * (3.0 - 2.0 * t)

    n00 = noise(x0, y0)
    n01 = noise(x0, y1)
    n10 = noise(x1, y0)
    n11 = noise(x1, y1)

    ix0 = n00 + (n10 - n00) * s
    ix1 = n01 + (n11 - n01) * s

    return ix0 + (ix1 - ix0) * t


def func(x, y):
    octaves = 6  # Количество октав шума
    persistence = 0.6  # Постоянство шума
    scale = 5.0  # Масштаб шума

    total = 0.0
    amplitude = 1.0
    frequency = 1.0
    max_value = 0.0

    # Суммирование октав шума Perlin
    for _ in range(octaves):
        tx = x * scale * frequency
        ty = y * scale * frequency

        total += val_noise(tx, ty) * amplitude
        max_value += amplitude
        amplitude *= persistence
        frequency *= 2.0

    total /= max_value
    # Коррекция и ограничение значения total
    total = (total - 0.35) * 1.85
    total = max(0, min(1, total))

    return (total, total, 255)


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
