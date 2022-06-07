from random import randint
from time import sleep

jogadores = dict()
for c in range(0, 4):
    numero = randint(1, 6)
    jogadores[f'jogador{c + 1}'] = numero

print('Valores sorteados')
for key, value in jogadores.items():
    print('{:>5}'.format(f'O {key} tirou {value}'))
    sleep(1)

contador = 1
print('Ranking dos jogadores:')
for jogador in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{contador:>5}º: {jogador} com {jogadores[jogador]}')
    contador += 1
    sleep(1)