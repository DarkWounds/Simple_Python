import random
numar = random.randint(1, 100)  # genereaza random intre 1 si 100

nrIncercari = 1

print("=== Ghici numarul ===")

nr = int(input("Introdu un numar intre 1 si 100: "))

while nr != numar:
    if nr < numar:
        print("Numarul este prea mic")
    else:
        print("Numarul este prea mare")
    nrIncercari += 1
    nr = int(input("Introdu un numar intre 1 si 100: "))

print(f"Felicitari! Ai ghicit numarul {numar} in {nrIncercari} incercari!")