
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Parameters
frames = 200
omega = 2 * np.pi * 0.1  # angular frequency
k = 2 * np.pi / 1.0  # wave number
phi = 0.0  # phase
amplitude = 1.0

# Spinor phase element (complex)
def spinor_wave(x, t):
    return np.exp(1j * (k * x - omega * t + phi))

# Light cone simulation function (2D plane radial pulse)
def light_cone_pattern(X, Y, t):
    R = np.sqrt(X**2 + Y**2)
    return amplitude * np.cos(k * R - omega * t)

# Grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Setup plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()
    Z = light_cone_pattern(X, Y, frame * 0.1)
    ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
    ax.set_zlim(-2, 2)
    ax.set_title(f"AM-GIO: Harmonic Spin-Light Field | Frame {frame}", color='cyan')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Amplitude")

ani = FuncAnimation(fig, update, frames=frames, interval=100)
plt.show()
