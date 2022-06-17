##########################################################################################
#                                   Valida a entrada do valor                            #
##########################################################################################

from posixpath import split
import string


def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).strip()
        is_monetario = True
        if not valor.isnumeric():
            for c in valor:
                if c.isalpha():
                    is_monetario = False
                    break
        if is_monetario and valor != '':
            break
        print(f'ERRO: "{valor}" é um preço inválido!')
    
    if ',' in valor:
        valor = valor.replace(',', '.')
    return float(valor)