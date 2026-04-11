print("=== Calculator ===")

a = float(input("Primul numar: "))
b = float(input("Al doilea numar: "))

print("Operatii:")
print("1. Adunare")
print("2. Scadere")
print("3. Inmultire")
print("4. Impartire")

optiune = input("Alege operatia (1-4): ")

if optiune == "1":
    print("Rezultat:", a + b)
elif optiune == "2":
    print("Rezultat:", a - b)
elif optiune == "3":
    print("Rezultat:", a * b)
elif optiune == "4":
    if b != 0:
        print("Rezultat:", a / b)
    else:
        print("Eroare: impartire la zero!")
else:
    print("Optiune invalida!")