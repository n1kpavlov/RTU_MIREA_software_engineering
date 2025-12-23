import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / h, y / w)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def smoothstep(edge0, edge1, x):
    t = max(0.0, min(1.0, (x - edge0) / (edge1 - edge0)))
    return t * t * (3.0 - 2.0 * t)


def func(x, y):
    r_red = 0.3
    r_green = 0.3
    blur_size = 0.25

    d_red = math.hypot(x - 0.52, y - 0.52)
    d_green = math.hypot(x - 0.48, y - 0.48)

    t_red = 1.0 - smoothstep(r_red - blur_size, r_red, d_red)
    t_green = 1.0 - smoothstep(r_green - blur_size, r_green, d_green)

    return (
        t_red, 
        t_green,
        0.0
    )


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
