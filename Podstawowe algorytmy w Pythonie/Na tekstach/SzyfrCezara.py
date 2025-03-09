def szyfruj(t, k):
    zaszyfrowany = ""
    for l in t:
        litera = k + ord(l)
        if litera > ord('z'):
            litera -= 26
        elif litera < ord('a'):
            litera += 26
        zaszyfrowany += chr(litera)
    return zaszyfrowany

tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = int(input("Podaj klucz szyfrowania: "))

print(f'Zaszyfrowany tekst: {szyfruj(tekst,klucz)}')