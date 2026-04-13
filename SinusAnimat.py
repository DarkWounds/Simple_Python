import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)

linie, = ax.plot([], [])
linie2, = ax.plot([], [], color='red')

def animate(frame):
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x - frame * 0.1) # + frame spre stanga, - frame spre dreapta
    y2 = np.cos(x + frame * 0.1)
    linie.set_data(x, y1)
    linie2.set_data(x, y2)
    return linie, linie2,

ani = animation.FuncAnimation(fig, animate, frames=200, interval=16)
plt.show()