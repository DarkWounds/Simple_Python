import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
import numpy as np

# PID parameters
Kp = 2
Ki = 0.1
Kd = 0.05
setpoint = 1
dt = 0.1

# State
vitezaCurenta = 0
eroareAnterioara = 0
sumaErori = 0
timp = []
viteze = []

# Figura
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

linie, = ax.plot([], [], label="Viteza motor")
ax.axhline(y=setpoint, color='red', linestyle='--', label="Setpoint")
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.5)
ax.set_title("PID Simulator")
ax.set_xlabel("Timp (s)")
ax.set_ylabel("Viteza")
ax.legend()
ax.grid(True)

# Slider
ax_kp = plt.axes([0.2, 0.02, 0.6, 0.03])
slider_kp = Slider(ax_kp, 'Kp', 0.0, 3.0, valinit=Kp)
slider_kd = Slider(plt.axes([0.2, 0.06, 0.6, 0.03]), 'Kd', 0.0, 0.1, valinit=Kd)
slider_ki = Slider(plt.axes([0.2, 0.10, 0.6, 0.03]), 'Ki', 0.0, 0.5, valinit=Ki)

def update(val):
    global vitezaCurenta, eroareAnterioara, sumaErori, timp, viteze
    # Resetezi simularea cand schimbi sliderul
    vitezaCurenta = 0
    eroareAnterioara = 0
    sumaErori = 0
    timp.clear()
    viteze.clear()

slider_kp.on_changed(update)
slider_kd.on_changed(update)
slider_ki.on_changed(update)

def animate(frame):
    global vitezaCurenta, eroareAnterioara, sumaErori

    kp = slider_kp.val
    kd = slider_kd.val
    ki = slider_ki.val

    eroare = setpoint - vitezaCurenta
    P = kp * eroare
    sumaErori += eroare * dt
    I = ki * sumaErori
    D = kd * (eroare - eroareAnterioara) / dt
    vitezaCurenta += (P + I + D) * dt

    timp.append(len(timp) * dt)
    viteze.append(vitezaCurenta)

    linie.set_data(timp, viteze)
    eroareAnterioara = eroare
    return linie,

anim = animation.FuncAnimation(fig, animate, interval = 50, blit = True)
plt.show()