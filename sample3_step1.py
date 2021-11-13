# Sample3 step1 (same as the step3 of sample3)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(f):
    y1 = np.sin(x - f)
    sine_curve.set_ydata(y1)


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid()
x = np.linspace(0, 10, 100)
y = np.sin(x)
sine_curve, = ax1.plot(x, y)

anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()
