import random
numar = random.randint(1, 100)  # genereaza random intre 1 si 100

nr = int(input("Introdu un numar intre 1 si 100: "))

print("=== Ghici numarul ===")

while (nr != numar):
    if (nr < numar):
        print("Numarul este prea mic")
    else:
        print("Numarul este prea mare")
    nr = int(input("Introdu un numar intre 1 si 100: "))

print("Felicitari! Ai ghicit numarul!")    