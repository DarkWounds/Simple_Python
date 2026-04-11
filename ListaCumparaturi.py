tasks = []  

print("------- Cumparaturi -------")

while True:
    optiune = int(input("Alege o optiune: "))
    if optiune == 1:
        task = input("Nume task: ")
        tasks.append(task)
    elif optiune == 2:
        task = input("Nume task: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task-ul nu exista.")
    elif optiune == 3:
        print("Lista de taskuri:")
        for task in tasks:
            print(task)
    elif optiune == 4:
        break
    else:      
        print("Optiune invalida. Incearca din nou.")        
        
print("La revedere!")                    