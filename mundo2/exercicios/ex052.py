n = int(input('Número: '))
divisiveis = []
cont = 0
for i in range(1, n+1):
    if n % i == 0:
        cont += 1
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(i, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('Portando, ele é primo.')
else:
    print('Portando, ele não é primo.')