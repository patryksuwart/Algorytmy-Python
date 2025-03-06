import math

def czyDoskonala(n):
    suma = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            suma += i + n/i
    if n == math.sqrt(n)**2:
        suma -= math.sqrt(n)
    if n == suma:
        return f"Liczba {n} jest liczbą doskonałą"
    else:
        return f"Liczba {n} nie jest liczbą doskonałą"

liczba = int(input("Podaj liczbę żeby sprawdzić czy jest ona liczbą doskonałą: "))

print(czyDoskonala(liczba))