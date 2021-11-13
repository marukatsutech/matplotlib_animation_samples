# Sample3 step3
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def update(f):
    y1 = np.sin(x - f)
    sine_curve.set_ydata(y1)


fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()
x = np.linspace(0, 10, 100)
y = np.sin(x)
sine_curve, = ax1.plot(x, y)

root = tk.Tk()
root.title("Sample3")
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack()

btn = tk.Button(root, text="Play/Pause")
btn.pack()

anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
