import math

def czyPierwsza(n):
    if n < 2:
        return f"Liczba {n} nie jest liczbą pierwszą."
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return f"Liczba {n} nie jest liczbą pierwszą."
    return f"Liczba {n} jest liczbą pierwszą"

liczba = int(input("Podaj liczbę żeby sprawdzić czy jest ona liczbą pierwszą: "))

print(czyPierwsza(liczba))