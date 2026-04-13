import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Crearea graficului

# Adăugarea liniilor
plt.plot(x, y1, label="Linia 1")
plt.plot(x, y2, label="Linia 2")

# Adăugarea punctelor
plt.scatter(x, y1, color="red")

# Adăugarea titlului și a etichetelor
plt.title("Grafic Simplu")
plt.legend()

# Graf 2

plt.figure()
categorii = ["Motor1", "Motor2", "Motor3"]
valori = [435, 300, 6000]
plt.bar(categorii, valori, color="blue")

# Grafic 4
plt.figure()

# np.linspace(start, stop, nr_puncte)
x = np.linspace(0, 10, 200)
y = np.sin(x)
plt.plot(x, y)
plt.grid(True)

plt.axhline(y=0, color='red', linestyle='--')  # linie orizontala
plt.title("Sinus")
plt.xlabel("Timp")
plt.ylabel("Valoare")

plt.show()