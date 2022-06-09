jogador = dict()
lista_jogadores = list()
while True:
    print('-' * 50)
    jogador['nome'] = str(input('Nome do jogador: '))
    qtd_partidas = int(input(f'Quantidade de partidas que {jogador["nome"]} jogou? '))

    gols_por_partida = list()
    for partida in range(qtd_partidas):
        gols_por_partida.append(int(input(f'Quantidade de gols na partida {partida + 1}: ')))

    jogador['aproveitamento'] = {'qtd_partidas': qtd_partidas}
    jogador['aproveitamento']['gols_por_partida'] = gols_por_partida[:]
    gols_por_partida.clear()
    jogador['aproveitamento']['total_gols'] = sum(jogador['aproveitamento']['gols_por_partida'])
    lista_jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break

print('-=' * 60)

print(f'{"cod":<5} {"nome":<5} {"gols":>15} {"total":>15}')
print('-' * 60)

for p, j in enumerate(lista_jogadores):
    print(f'{p:<5} {j["nome"]:<5} {str(j["aproveitamento"]["gols_por_partida"]):>15} {j["aproveitamento"]["total_gols"]:>15}')
print('-' * 60)

while True:
    codigo_jogador = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if codigo_jogador == 999:
        break
    elif codigo_jogador > len(lista_jogadores) - 1 or codigo_jogador < 0:
        print(f'ERRO! Não existe jogador com código {codigo_jogador}! Tente novamente')
        print('-' * 60)
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista_jogadores[codigo_jogador]["nome"]}:')
        for posicao, qtd_gols in enumerate(lista_jogadores[codigo_jogador]["aproveitamento"]["gols_por_partida"]):
            print(f'No jogo {posicao} fez {qtd_gols} gols.')
        print('-' * 60)

print('<< VOLTE SEMPRE >>')
