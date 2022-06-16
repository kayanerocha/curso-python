##########################################################################################
#                       Modifica as funções do 107 para receber mais um parâmetro        #
#                                   e saber se formata ou não a moeda                    #
##########################################################################################

from ex109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, tempos {moeda.diminuir(p, 13, True)}')