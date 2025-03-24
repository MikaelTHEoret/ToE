
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

nx, ny = 100, 100
dx = dy = 1.0
c = 1.0
dt = 0.1
steps = 200

phi = np.zeros((nx, ny))
phi_new = np.zeros_like(phi)
phi_old = np.zeros_like(phi)
phi[nx//2, ny//2] = 1.0

def laplacian(f):
    return (np.roll(f, 1, axis=0) + np.roll(f, -1, axis=0) +
            np.roll(f, 1, axis=1) + np.roll(f, -1, axis=1) - 4 * f) / dx**2

fig, ax = plt.subplots()
im = ax.imshow(phi, cmap='plasma', interpolation='bilinear', vmin=-1, vmax=1)
ax.set_title("AUM Field Simulation (2D Wave Equation)")
ax.axis('off')

def update(frame):
    global phi, phi_old, phi_new
    lap = laplacian(phi)
    phi_new = 2 * phi - phi_old + (c * dt)**2 * lap
    phi_old, phi = phi, phi_new
    im.set_array(phi)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=steps, blit=True, repeat=False)
plt.show()
