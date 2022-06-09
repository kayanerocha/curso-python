##########################################################################################
#               Ordenando um dicionário: jogo de dados e fazendo ranking do maior        #
#                                       para o menor                                     #
##########################################################################################

from random import randint
from time import sleep

jogadores = dict()
for c in range(0, 4):
    numero = randint(1, 6)
    jogadores[f'jogador{c + 1}'] = numero

print('Valores sorteados')
for key, value in jogadores.items():
    print(f'O {key} tirou {value}')
    sleep(1)

print('-=' * 30)
contador = 1
print('  Ranking dos jogadores:')
for jogador in sorted(jogadores, key=jogadores.get, reverse=True): # (jogadores.items(), key=itemgetter(1), reverse=True)
    print(f'{contador:>5}º: {jogador} com {jogadores[jogador]}')
    contador += 1
    sleep(1)