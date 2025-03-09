def wzorzec(w, t):
    dlt = len(t)
    dlw = len(w)
    licznik = 0
    for i in range(dlt):
        j = 0
        while j < dlw and t[i+j] == w[j]: j+=1
        if j == dlw:
            licznik+=1
    return licznik

tekst = input("Podaj tekst: ")
wz = input("Podaj wzorzec: ")

print(f'Wzorzec wystąpił w tekście {wzorzec(wz, tekst)} razy')