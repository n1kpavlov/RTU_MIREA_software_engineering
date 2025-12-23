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


def func(x, y):
    cx, cy = 0.5, 0.5
    radius = 0.4
    mouth_angle = 30

    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    angle = math.degrees(math.atan2(y - cy, x - cx))

    if distance <= radius:
        if -mouth_angle <= angle <= mouth_angle:
            return (0, 0, 0)
        else:
            eye_radius = 0.05
            eye_x, eye_y = 0.6, 0.25
            if ((x - eye_x) ** 2 + (y - eye_y) ** 2) <= eye_radius ** 2:
                return (0, 0, 0)
            return (1, 1, 0)
    else:
        return (0, 0, 0)


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
