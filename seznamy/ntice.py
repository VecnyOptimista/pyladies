"""==== POUZITI VE FUNKCI ===="""
def ntice_ve_funkci(logicka, retezec):
    # Vracime ntici se dvema ruznymi hodnotami.
    upraveny_retezec = '{} člověče'.format(retezec)
    return logicka, upraveny_retezec

# Navratove hodnoty funkce (n-tici) muzeme ulozit bud do jedne promenne
spolecna_promenna = ntice_ve_funkci(True, 'Ahoj')
print('Spolecna promenna pro obe navratove hodnoty:', spolecna_promenna)

# Nebo tyto hodnoty rozdelime kazdou do sve promenne
logicka, retezec = ntice_ve_funkci(True, 'Ahoj')
print('Prvni vracena hodnota:', logicka)
print('Druha vracena hodnota:', retezec)

"""==== DEFINICE N-TIC ===="""
promenna = 1, 2, 3, 'Ahoj'  # Muze, ale nemusi obsahovat zavorky kolem ()

prazdna_ntice = ()

jednotkova_ntice = ('Ahoj', )  # Tady zavorky psat musime, dokonce je povinna i carka.
# Mezera za carkou uz povinna neni, ale patri do pravidel PEP8, jak spravne formatovat Python kod :)
