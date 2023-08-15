# Sample3 step5
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    if is_play:
        y1 = np.sin(x - f)
        sine_curve.set_ydata(y1)


is_play = False

fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()
x = np.linspace(0, 10, 100)
y = np.sin(x)
sine_curve, = ax1.plot(x, y)

root = tk.Tk()
root.title("Sample3")
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

btn = tk.Button(root, text="Play/Pause", command=switch)
btn.pack()

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()

