import matplotlib.pyplot as plt
import numpy as np

@np.vectorize
def z(u, v):
    res = 0
    for m in range(-4, 5):
        for n in range(-4, 5):
            res +=  (1/81) * (np.e**(-1j * (m * u + n * v)))
    return abs(res)

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