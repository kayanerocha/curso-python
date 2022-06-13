##########################################################################################
#                   Função que recebe vários parâmetros e diz qual o maior               #
##########################################################################################
from time import sleep

def maior(*valores):
    print('-=' * 30)
    print('Analisando os valores passados...')

    for v in valores:
        print(v, end=' ')

    print(f'Foram informados {len(valores)} valores ao todo.')
    maior = max(valores) if len(valores) > 0 else 0
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()