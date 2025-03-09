print('Jesteśmy {}, którzy mówią "{}!"'.format('rycerzami', 'Ni'))
print('{0} i {1}'.format('mielonka', 'jajka'))
print('{1} i {0}'.format('mielonka', 'jajka'))
print('Ta {food} jest {adjective}.'.format(food = 'mielonka', adjective = 'absolutnie okropna'))
print('Historia {0}, {1} i {other}.'.format('Billa', 'Manfreda', other='Georga'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

table = {k: str(v) for k, v in vars().items()} #vars zwraca słownik zawierający wszystkie zmienne lokalne
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
print(message.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))