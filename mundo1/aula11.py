####################################################
#            #11 - Cores no Terminal               #
####################################################

"""
módulo color rise
ANSI escape sequence
\033[<style>;<text-color>;<background>m  # sempre que quiser representar uma cor, os códigos são opcionais
\033[m  # volta o terminal para o padrão
style
    0: none - default
    1: bold
    4: underline
    7: negative - inverte a cor da letra e de fundo
text-color
    30: branco
    31: vermelho
    32: verde
    33: amarelo
    34: azul
    35: magenta, lilás
    36: ciano, azul claro
    37; cinza - default
background:
    40 a 47 como text-color
"""

'''
print('\033[1;31;43mOlá, mundo!\033[m')  # a formatação para onde tem o código final
print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[30mOlá, mundo!\033[m')
print('\033[7;30mOlá, mundo!\033[m')
print('\033[0;33;44mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')
'''

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Kayane'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
