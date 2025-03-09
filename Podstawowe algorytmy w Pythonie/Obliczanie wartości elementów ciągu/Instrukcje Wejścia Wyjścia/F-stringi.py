#f-stringi
import math
print(f'Wartość pi wynosi w przybliżeniu {math.pi:.3f}')
table = {'Sjoerd':4127, 'Jack':4098, 'Dcab':7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
animals = 'węgorze'
print(f'Na moim poduszkowcu są {animals}')
print(f'Na moim poduszkowcu są {animals!r}')
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')