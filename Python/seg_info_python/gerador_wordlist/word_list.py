import itertools

string = input('String a ser permutada: ')
resultado = itertools.permutations(string, len(string))
#resultado = itertools.permutations('abc',3)

for i in resultado:
    print(''.join(i))
