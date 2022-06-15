##########################################################################################
#                   Função que valida se a entrada do usuário é um int                   #
##########################################################################################

from glob import glob
import string


def leiaInt(mensagem):
    """
    -> Valida se a entada é um inteiro.
    :param mensagem: mensagem que solicita a entrada.
    :return: o número informado pelo usuário.
    """
    while True:   
        numero = input(f'{mensagem}').strip()
        if numero in '0123456789' and len(numero) > 0:
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return numero

numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')