# ============================================
# TIPURI DE AFISARE IN PYTHON
# ============================================

nume = "Andrei"
varsta = 17
inaltime = 1.75
pi = 3.14159

# ── 1. Print simplu ──────────────────────────
print("Hello World!")
print(nume)

# ── 2. Print cu virgula (spatiu automat) ─────
print("Nume:", nume, "Varsta:", varsta)
# Output: Nume: Andrei Varsta: 17

# ── 3. Concatenare cu + ──────────────────────
print("Nume: " + nume + " Varsta: " + str(varsta))
# str() necesar pentru numere!

# ── 4. F-string (cel mai folosit) ────────────
print(f"Nume: {nume}, Varsta: {varsta}")
# Output: Nume: Andrei, Varsta: 17

# ── 5. F-string cu calcule ───────────────────
print(f"Peste 3 ani voi avea {varsta + 3} ani")

# ── 6. Zecimale ──────────────────────────────
print(f"Pi cu 2 zecimale: {pi:.2f}")
print(f"Pi cu 4 zecimale: {pi:.4f}")
print(round(pi, 2))

# ── 7. Aliniere text ─────────────────────────
print(f"{'Stanga':<10} {'Centru':^10} {'Dreapta':>10}")
# Output: Stanga      Centru      Dreapta
# < = aliniere stanga, ^ = centru, > = dreapta

# ── 8. Separator si end ──────────────────────
print("a", "b", "c", sep="-")        # a-b-c
print("Prima linie", end=" ")        # fara newline
print("Aceeasi linie")               # Prima linie Aceeasi linie

# ── 9. Caractere speciale ─────────────────────
print("Linie 1\nLinie 2")            # \n = newline
print("Tab\tTab")                    # \t = tab
print("Ghilimele: \"citat\"")        # \" = ghilimele

# ── 10. Print lista si dict ──────────────────
lista = [1, 2, 3, 4, 5]
print(lista)                         # [1, 2, 3, 4, 5]
print(*lista)                        # 1 2 3 4 5 (unpacking)
print(*lista, sep=", ")              # 1, 2, 3, 4, 5

dictionar = {"nume": "Andrei", "varsta": 17}
print(dictionar)                     # {'nume': 'Andrei', 'varsta': 17}

# ── 11. Formatare numar mare ─────────────────
numar_mare = 1000000
print(f"{numar_mare:,}")             # 1,000,000
print(f"{numar_mare:_}")             # 1_000_000

# ── 12. Bool ─────────────────────────────────
activ = True
print(f"Activ: {activ}")             # Activ: True
print(f"Activ: {str(activ).lower()}") # Activ: true

# ── 13. Multiline print ──────────────────────
print("""
Linie 1
Linie 2
Linie 3
""")