def input_numar(mesaj):
    while True:
        try:
            numar = int(input(mesaj))
            print("Validare reusita.")
            return numar
        except ValueError:
            print("Numar invalid.")
        
    
numar = input_numar("Introduceti un numar: ")
print(f"Ai introdus: {numar}")  