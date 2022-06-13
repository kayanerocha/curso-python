##########################################################################################
#                   Função que sorteia 5 número e outra que soma os números pares        #
##########################################################################################
from random import randint

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    numeros = list()
    for c in range(5):
        numero = randint(0, 10)
        print(numero, end=' ')
        numeros.append(numero)
    print('PRONTO!')
    
    return numeros

def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    
    print(f'Somando os valores pares de {numeros}, temos {soma}')

somaPar(sorteia())
    

