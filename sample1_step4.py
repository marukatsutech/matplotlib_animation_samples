# Sample1 step4
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(f):
    ax1.cla()
    ax1.grid()
    y = np.sin(x - f)
    ax1.plot(x, y)


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid()
x = np.linspace(0, 10, 100)

anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()
