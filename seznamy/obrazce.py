def prazdny_obrazec():
    seznam = []
    for radek in range(5):
        seznam.append(5 * ["O"])
    return seznam

def tiskni_obrazec(seznam):
    for radek in seznam:
        print(" ".join(radek))
    print()

# Prazdny obrazec
tiskni_obrazec(prazdny_obrazec())

# Prvni dva radky plne
seznam = prazdny_obrazec()
seznam[0:2] = [5 * 'X', 5 * 'X']
tiskni_obrazec(seznam)

# Tri X uprostred
seznam_2 = prazdny_obrazec()
seznam_2[2][1:4] = ['X', 'X', 'X']
tiskni_obrazec(seznam_2)

# Pismeno N + Pocet X a O v prostrednim radku
seznam_3 = prazdny_obrazec()
for cislo_r, radek in enumerate(seznam_3):
    for cislo_b, bunka in enumerate(radek):
        if cislo_b in [0, 4] or cislo_b == cislo_r:
            seznam_3[cislo_r][cislo_b] = 'X'
tiskni_obrazec(seznam_3)

# Zjisteni poctu jednotlivych znaku v prostrednim radku obrazce 3 pomoci metody .count()
print('Pocet X v prostrednim radku:', seznam_3[2].count("X"))
print('Pocet O v prostrednim radku:', seznam_3[2].count("O"))
print()

# Pismeno Z
seznam_4 = prazdny_obrazec()
for cislo_r, radek in enumerate(seznam_4):
    for cislo_b, bunka in enumerate(radek):
        if cislo_r == 0 or cislo_r == 4 or cislo_r + cislo_b == len(seznam_4) - 1:
            seznam_4[cislo_r][cislo_b] = 'X'
tiskni_obrazec(seznam_4)

# Kostka
seznam_5 = prazdny_obrazec()
for cislo_r, radek in enumerate(seznam_5):
    for cislo_b, bunka in enumerate(radek):
        if cislo_r in range(1, 4) and cislo_b in range(1, 4):
            seznam_5[cislo_r][cislo_b] = 'X'
tiskni_obrazec(seznam_5)
