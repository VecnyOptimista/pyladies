# Retezec, se kterym budeme pracovat. Musime si ho ale prevest na seznam
retezec = 'příšerně žluťoučký kůň úpěl ďábelské ódy na bílý měsíc'

# Rozdeleni retezce na jednotliva slova do seznamu
seznam = retezec.split(' ')  # staci i samotne retezec.split()
print(seznam)

# Zjistime pocet slov v celem seznamu
print('Pocet slov:', len(seznam))

# Pomoci count muzeme zjistovat pocet vyskytu hledaneho slova. Zde ho mame pouze jednou
print('Pocet vyskytu slova kůň ve vete:', seznam.count('kůň'))

# Overeni pritomnosti slova
print('Je slovo kůň ve vete:', 'kůň' in seznam)

# Umisteni slova v seznamu
print('Umisteni slova kůň v seznamu:', seznam.index('kůň'))

# CO SE STANE, KDYZ BUDEME ZJISTOVAT INDEX NEEXISTUJICIHO?
# Prvek neni v seznamu - metoda index vyhodi ValueError v pripade, ze slovo nenajde
# print('Hledani neexistujiciho slova v seznamu:', seznam.index('slon'))

# Spojeni seznamu zpet do jednoho retezce pomoci jineho oddelovace
print('Spojeno do retezce: ', '-'.join(seznam))
