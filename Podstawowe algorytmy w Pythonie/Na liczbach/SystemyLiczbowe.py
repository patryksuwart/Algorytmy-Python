def dwojkowyNaDziesietny(n):
    return int(n, 2)

def dziesietnyNaDwojkowy(n):
    return bin(int(n)) #oct() hex()

liczba1 = input("Podaj liczbę do konwersji: ")

print(dziesietnyNaDwojkowy(liczba1))

liczba2 = input("Podaj liczbę do konwersji: ")

print(dwojkowyNaDziesietny(liczba2))