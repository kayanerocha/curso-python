# --------------------------------------------------#
#          #14 - Estrutura de Repetição while       #
# --------------------------------------------------#
# serve para quando sei e não sei o limite

"""
i = 1
while i < 10:
    print(i)
    i += 1
"""

'''
n = 1
while n != 0:  # flag, condição de parada
    n = int(input('Digite um valor: '))
print('Fim')
'''

'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
'''

n = 1
par = impar = 0
while n != 0:  # flag, condição de parada
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Vpcê digitou {} números pares e {} números ímpares.'.format(par, impar))