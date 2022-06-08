jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
qtd_partidas = int(input(f'Quantidade de partidas {jogador["nome"]} jogou? '))

gols_por_partida = list()
for partida in range(qtd_partidas):
    gols_por_partida.append(int(input(f'Quantidade de gols na partida {partida + 1}: ')))

jogador['aproveitamento'] = {'qtd_partidas': qtd_partidas}
jogador['aproveitamento']['gols_por_partida'] = gols_por_partida
jogador['aproveitamento']['total_gols'] = sum(jogador['aproveitamento']['gols_por_partida'])

print('-=' * 60)
print(jogador)
print('-=' * 60)

for key, value in jogador.items():
    if key not in 'aproveitamento':
        print(f'O campo {key} tem o valor {value}')
    else:
        for key, value in jogador['aproveitamento'].items():
            print(f'O campo {key} tem o valor {value}')

print('-=' * 60)

print(f'O jogador {jogador["nome"]} jogou {jogador["aproveitamento"]["qtd_partidas"]} partidas.')
for partida in range(jogador['aproveitamento']['qtd_partidas']):
    print(f'     => Na partida {partida + 1}, fez {jogador["aproveitamento"]["gols_por_partida"][partida]} gols.')

print(f'Foi um total de {jogador["aproveitamento"]["total_gols"]} gols.')
