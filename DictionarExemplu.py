motor = {
    "nume": "Shoot",
    "rpm": 5000,
    "putere": 100
}

print(motor["nume"])
print(motor.get("nume", -1)) # Daca nu exista cheia, se returneaza -1
print(motor.get("rpm", -1))
print(motor.get("putere", -1))   
print(motor.get("cuplu", -1))
# print(motor["cuplu"])  # fara .get(), eroare daca nu exista cheia

motor["cuplu"] = 1.47      # adauga cheie noua
del motor["putere"]        # sterge cheie

# Iterare prin chei
for cheie, valoare in motor.items():
    print(f"{cheie}: {valoare}")
    