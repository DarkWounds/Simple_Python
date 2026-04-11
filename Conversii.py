def Aduna(a, b):
    return a + b

def Scade(a, b):
    return a - b

def ConversieCmInch(cm):
    return cm / 2.54

def ConversieInchCm(inch):
    return inch * 2.54

def ConversieCelsiusFahrenheit(celsius):
    return (celsius * 9/5) + 32

def ConversieFahrenheitCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def ConversieKmMile(km):
    return km / 1.60934
   
def ConversieMileKm(mile):
    return mile * 1.60934

print("-------- Meniu de conversii -------")
print("1. Adunare")
print("2. Scadere")
print("3. Conversie cm in inch")
print("4. Conversie inch in cm")
print("5. Conversie Celsius in Fahrenheit")
print("6. Conversie Fahrenheit in Celsius")
print("7. Conversie km in mile")
print("8. Conversie mile in km")
print("9. Iesire")

while True:
    
    optiune = input("Alege o optiune (1-9): ")
    
    if(optiune == '1'):
        a = float(input("Introdu primul numar: "))
        b = float(input("Introdu al doilea numar: "))
        print("Rezultatul adunarii este:", Aduna(a, b))
    elif(optiune == '2'):
        a = float(input("Introdu primul numar: "))
        b = float(input("Introdu al doilea numar: "))
        print("Rezultatul scaderii este:", Scade(a, b))
    elif(optiune == '3'):
        cm = float(input("Introdu lungimea in cm: "))
        print("Rezultat:", round(ConversieCmInch(cm), 2))
    elif(optiune == '4'):
        inch = float(input("Introdu lungimea in inch: "))
        print("Rezultat:", round(ConversieInchCm(inch), 2))
    elif(optiune == '5'):
        celsius = float(input("Introdu temperatura in Celsius: "))
        print("Temperatura in Fahrenheit este:", round(ConversieCelsiusFahrenheit(celsius), 2))                
    elif(optiune == '6'):
        fahrenheit = float(input("Introdu temperatura in Fahrenheit: "))
        print("Temperatura in Celsius este:", round(ConversieFahrenheitCelsius(fahrenheit), 2))
    elif(optiune == '7'):
        km = float(input("Introdu distanta in km: "))
        print("Distanta in mile este:", round(ConversieKmMile(km), 2))
    elif(optiune == '8'):
        mile = float(input("Introdu distanta in mile: "))
        print("Distanta in km este:", round(ConversieMileKm(mile), 2))
    elif(optiune == '9'):
        break
    else:
        print("Optiune invalida. Te rog sa alegi o optiune valida (1-9).")
        
print("Programul s-a incheiat. La revedere!")        