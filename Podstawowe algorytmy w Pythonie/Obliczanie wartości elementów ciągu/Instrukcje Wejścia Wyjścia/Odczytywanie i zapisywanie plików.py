with open('plikroboczy.txt', encoding="utf-8") as f:
    print(f.read())
print(f.closed) #automatyczne zamknięcie pliku

print()

with open('plikroboczy.txt', encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
print(f.closed)

print()

with open('plikroboczy.txt', encoding="utf-8") as f:
    for line in f:
        print(line, end='')

with open('plikroboczy.txt', 'r+', encoding="utf-8") as f:
    f.write('Test')

f = open('plikroboczy.txt', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)  # Idź do szóstego bajtu w pliku
f.read(1)
f.seek(-3, 2)  # Idź do trzeciego bajtu przed końcem
f.read(1)