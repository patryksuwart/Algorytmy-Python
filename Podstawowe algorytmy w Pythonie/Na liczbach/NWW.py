def NWD(a, b):
    while a != b:
        if a > b: a-=b
        else: b-=a
    return a

def NWW(a, b):
    return a*b/NWD(a, b)

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print(f"Najmniejsza wspólna wielokrotność to: {NWW(a,b)}")