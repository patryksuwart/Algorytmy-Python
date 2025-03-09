def NWD(a, b):
    while a != b:
        if a > b: a-=b
        else: b-=a
    return f'Największy wspólny dzielnik: {a}'

a = int(input("Podaj pierwszą liczbę: "))

b = int(input("Podaj drugą liczbę: "))

print(NWD(a,b))