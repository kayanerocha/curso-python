##########################################################################################
#                   Função que sorteia 5 número e outra que soma os números pares        #
##########################################################################################
from random import randint
from time import sleep

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    numeros = list()
    for c in range(5):
        numero = randint(0, 10)
        numeros.append(numero)
        print(numero, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    
    return numeros

def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    
    print(f'Somando os valores pares de {numeros}, temos {soma}')

somaPar(sorteia())
    

