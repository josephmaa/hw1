import matplotlib.pyplot as plt
import numpy as np

@np.vectorize
def z(u, v):
    return abs(0.01 / (1-0.9*(np.e**(-1j*u))-0.9*(np.e**(-1j*v))+0.81*(np.e**(-1j*u-1j*v))))

x = np.linspace(-np.pi, np.pi, 200)
y = np.linspace(-np.pi, np.pi, 200)
X, Y = np.meshgrid(x, y)
Z = z(X, Y)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(Y, X, Z)
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel('z')
plt.show()