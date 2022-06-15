##########################################################################################
#                   Função que valida se a entrada do usuário é um int                   #
##########################################################################################

from glob import glob
import string


def leiaInt(mensagem):
    while True:   
        numero = input(f'{mensagem}').strip()
        if numero in '0123456789' and len(numero) > 0:
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return numero

numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')