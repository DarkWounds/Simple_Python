import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Limite x y, axe
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Desenaree minge val goala, val goala, 'bo' (albastru), markersize = 20 (marimea)
#minge, returneaza o lista, nu un obiect
minge, = ax.plot([], [], 'bo', markersize=20)  # cerc albastru

y = 10.0
viteza = 0.0

def animate(frame):
    
    global y, viteza
    
    viteza -= 0.01      # gravitatie
    y += viteza        # miscare
    
    if y <= 0:
        y = 0
        viteza = abs(viteza) * 0.75  # bounce
    
    minge.set_data([5], [y])
    return minge,

ani = animation.FuncAnimation(fig, animate, frames=200, interval=16) # interval 16 ~ 60 fps
plt.show()