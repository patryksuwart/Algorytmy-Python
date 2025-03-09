#metoda str() i repr()
s = 'Witaj, świecie.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'Wartość x to ' + repr(x) + ', i y to ' + repr(y) + '...'
print(s)
hello = 'witaj, świecie\n'
hellos = repr(hello)
print(hellos)
print(repr((x, y, ('mielonka', 'jajka'))))
