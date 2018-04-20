print("""==== TVORBA ====""")
retezec = 'příšerně žluťoučký kůň úpěl ďábelské ódy na bílý měsíc'
seznam = retezec.split(' ')  # Rozdelime retezec na jednotliva slova do seznamu
print(seznam)

# Rozkouzkovani retezce do seznamu
retezec_k_rozdeleni = 'ABCDEFGHIJK'
print(list(retezec_k_rozdeleni))

print("""==== VYBER ====""")
print(seznam[0])

# Vyber odzadu
print(seznam[-2])

print(seznam[-1])

# Rozsah polozek
print(seznam[1:4])

# Ohraniceni z prava
print(seznam[2:-3])

# Kazde druhe slovo
print(seznam[::2])

print("""==== PRIDAVANI ====""")
upravovany_seznam = ['puvodni_obsah']

# Spojeni seznamu
upravovany_seznam += ['pripojeny', 'seznam']

# Vkladani na konec
upravovany_seznam.append('appendovany_obsah')

# Vlozeni na zacatek
upravovany_seznam.insert(0, 'insertovany_obsah')

# Rozsireni
upravovany_seznam.extend(['extendovany_obsah1', 'extendovany_obsah2'])

print(upravovany_seznam)

print("""==== UPRAVA ====""")
# Pocet prvku, ktere misto puvodnich vkladame, nemusi byt stejny. Tim se muze i zmenit celkova velikost seznamu.
upravovany_seznam[1:3] = ['upraveny_obsah1', 'upraveny_obsah2']
print(upravovany_seznam)

print("""==== MAZANI ====""")
seznam_ke_smazani = ['A', 'B', 'C', 'D']
# Mazani prvku podle indexu
del seznam_ke_smazani[0]  # smaze prvni prvek
print(seznam_ke_smazani)

# Vybrani posledniho prvku seznamu. Tato metoda soucasne vrati hodnotu, kterou maze, na vystup.
print('Smazany prvek pomoci pop: ', seznam_ke_smazani.pop())  # smaze posledni prvek
print(seznam_ke_smazani)

seznam_ke_smazani.remove('C')
print(seznam_ke_smazani)

print("""==== RAZENI ====""")
# Budeme tridit puvodni vetu se "ze zacatku
trideny_seznam = retezec.split()  # Pripravime si novy seznam, ktery budeme radit.

# Defaultni razeni je vzestupne. Pozadavek je, aby seznam obsahoval prvky, ktere se daji v Pythonu porovnavat <, >
trideny_seznam.sort()
print('Vzestupne serazene:', trideny_seznam)

# Seznam muzeme radit i sestupne
trideny_seznam.sort(reverse=True)
print('Sestupne serazene:', trideny_seznam)

# Pri razeni python serazuje nejdrive celou abecedu velkych pismen a potom celou abecedu malych pismen. To se da obejit.
# Vyzaduje ale pouziti lambda funkce
# TODO
