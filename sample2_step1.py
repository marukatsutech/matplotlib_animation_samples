# Sample2 step1 (same as step1 of sample1)
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid()
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax1.plot(x, y)
plt.show()
