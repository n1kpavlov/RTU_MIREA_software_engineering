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
    color = noise(x, y)
    return (color, color, color)

def noise(x, y):
    return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1

label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()