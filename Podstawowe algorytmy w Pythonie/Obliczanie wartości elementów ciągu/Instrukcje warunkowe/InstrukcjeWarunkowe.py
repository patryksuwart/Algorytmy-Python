a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if a == b:
    print('Liczby są równe')
elif a+b > 10 and a+b < 15:
    print('Suma liczb jest większa niż 10 ale mniejsza niż 15')
elif a+b == 7 or a+b == 3:
    print('Suma liczb jest równa 7 lub 3')