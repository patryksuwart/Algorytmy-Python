def porownaj(t1, t2):
    dl1 = len(t1)
    dl2 = len(t2)
    if dl1 != dl2:
        return False
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True

tekst1 = input("Podaj pierwszy tekst: ")
tekst2 = input("Podaj drugi tekst: ")

print(porownaj(tekst1,tekst2))