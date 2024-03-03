geschenke = ('Playstation', 'Switch', 'Fortnite', 'Brettspiel Labyrinth', 'Brettspiel Siedler von Catan')
for geschenk in geschenke:
    print(geschenk)


index = 0
while index < len(geschenke):
    print(geschenke[index])
    index += 1


vergessenesgeschenk = ('Eislaufschuhe',)
geschenke += vergessenesgeschenk

vergessenesgeschenk_liste = list(vergessenesgeschenk)


print("Element 2 und 3:", geschenke[1:3])
