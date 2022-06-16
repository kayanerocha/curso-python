##################################################################################
#                                 Módulos e Pacotes                              #
##################################################################################

# ------------------------------ MODULARIZAÇÃO -----------------------------------

    # Divide um programa grande em pequenos módulos
    # Aumenta a legibilidade
    # Facilita a manutenção
    # Organiza o código
    # Ocultação de código detalhado
    # Permite reutilizar módulos em outros projetos
    # Todo arquivo .py é um módulo contanto que tenha funções internas
    # Exemplo de importação de um módulo: from random import randint (from modulo import funcao)

# Para utilizar o módulo uteis:
from uteis import fatorial, dobro, triplo

num = int(input('Digite um valor: '))
fat = fatorial(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}.')
print(f'O triplo de {num} é {triplo(num)}.')

# ------------------------------------ PACOTES ------------------------------------

    # É uma pasta que contém módulos, assim toda pasta é considerada um módulo
    # Utilizados caso os módulos fiquem grandes demais
    # Separa os módulos por assuntos: números, strings, datas, cores
    # Para importar: import uteis ou from uteis import datas (uteis -> pacote, datas -> módulo)
    # É possível ter um módulo dentro de outro:
        # uteis
            # cores
            # datas
            # numeros
            # strings
    # __init__.py: criado em cada módulo

# Para utilizar o pacote uteis/numeros:
from pacote_uteis import numeros
print(f'O fatorial de 5 é {numeros.fatorial(5)}')