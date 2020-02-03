import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.05)
y = np.sin(x)
z = np.cos(x)


def plotfun(a, b, c):
    plt.plot(a, b, a, c)
    plt.show()


plotfun(x, y, z)