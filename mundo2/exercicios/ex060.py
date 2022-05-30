from math import factorial

numero = int(input('Número: '))
fatorial = 1
print('O fatorial de {} é {}'.format(numero, factorial(numero)))

# outra forma
print('Calculando {}! = '.format(numero), end='')
while numero > 0:
    fatorial *= numero
    print('{}'.format(numero), end=' * ' if numero > 1 else ' = ')
    numero -= 1
print(fatorial)