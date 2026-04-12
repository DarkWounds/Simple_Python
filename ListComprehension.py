numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rezultatPar = [expresie for expresie in numere if expresie % 2 == 0]

#   Echivalent cu acesta:
#    rezultatPar = []
#    for expresie in numere:
#        if expresie % 2 == 0:
#            rezultatPar.append(expresie)
#

rezultatPatrat = [expresie * expresie for expresie in numere]

print("Numerele pare sunt:", rezultatPar)
print("Pătratele numerelor sunt:", rezultatPatrat)