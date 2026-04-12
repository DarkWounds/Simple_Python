# ============================================
# FUNCTII PENTRU STRINGURI IN PYTHON
# ============================================

text = "Hello, World!"

# ── 1. Lungime (strlen) ──────────────────────
print(len(text))                    # 13

# ── 2. Majuscule / Minuscule ─────────────────
print(text.upper())                 # HELLO, WORLD!
print(text.lower())                 # hello, world!
print(text.capitalize())            # Hello, world!
print(text.title())                 # Hello, World!

# ── 3. Cautare (strstr / indexOf) ────────────
print(text.find("World"))           # 7 (index unde incepe)
print(text.find("xyz"))             # -1 (nu exista)
print("World" in text)              # True
print("xyz" in text)                # False

# ── 4. Inlocuire (replace) ───────────────────
print(text.replace("World", "Python"))  # Hello, Python!

# ── 5. Split (imparte string in lista) ───────
propozitie = "unu doi trei patru"
cuvinte = propozitie.split(" ")     # imparte dupa spatiu
print(cuvinte)                      # ['unu', 'doi', 'trei', 'patru']
print(cuvinte[0])                   # unu

# ── 6. Join (uneste lista in string) ─────────
lista = ["unu", "doi", "trei"]
print(", ".join(lista))             # unu, doi, trei
print(" - ".join(lista))            # unu - doi - trei

# ── 7. Strip (sterge spatii) ─────────────────
text_spatii = "   Hello   "
print(text_spatii.strip())          # "Hello"
print(text_spatii.lstrip())         # "Hello   "
print(text_spatii.rstrip())         # "   Hello"

# ── 8. Inceput / Sfarsit ─────────────────────
print(text.startswith("Hello"))     # True
print(text.endswith("!"))           # True

# ── 9. Slicing (substring) ───────────────────
print(text[0:5])                    # Hello
print(text[7:12])                   # World
print(text[-1])                     # ! (ultimul caracter)
print(text[::-1])                   # !dlroW ,olleH (inversat)

# ── 10. Count ────────────────────────────────
print(text.count("l"))              # 3

# ── 11. Verificari ───────────────────────────
print("123".isdigit())              # True
print("abc".isalpha())              # True
print("abc123".isalnum())           # True
print("   ".isspace())              # True

# ── 12. Formatare ────────────────────────────
print("hello".center(20, "-"))      # -------hello--------
print("hello".ljust(20, "."))       # hello...............
print("hello".rjust(20, "."))       # ...............hello

# ── 13. Conversii ────────────────────────────
numar = 42
print(str(numar))                   # "42" (int -> string)
print(int("42"))                    # 42 (string -> int)
print(float("3.14"))                # 3.14 (string -> float)