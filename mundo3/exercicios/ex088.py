from random import choice
from time import sleep

print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
qtd_jogos = int(input('Quantidade de jogos desejada: '))

print('{:=^40}'.format(f' SORTEANDO {qtd_jogos} JOGOS '))
sleep(1)

numeros_possiveis = list()
jogo = list()
todos_jogos = list()
# sorteia 6 números por jogo
for j in range(qtd_jogos):
    # preenche a lista com os 60 números possíveis
    for num_possiveis in range(1, 61):
        numeros_possiveis.append(num_possiveis)

    # sorteia 6 números 
    for c in range(0, 6):
        num_escolhido = choice(numeros_possiveis)
        jogo.append(num_escolhido)
        numeros_possiveis.remove(num_escolhido) # remove para não repetir no mesmo jogo

    # adiciona na lista de jogos uma cópia do jogo feito
    jogo.sort()
    todos_jogos.append(jogo[:])
    jogo.clear()
    numeros_possiveis.clear() # limpa para no próximo loop adicionar novamente os 60 números

for p, jg in enumerate(todos_jogos):
    print(f'Jogo {p + 1}: {jg}')
    sleep(1)

print(f'{" < BOA SORTE! > ":=^40}')
