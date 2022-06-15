##########################################################################################
#                   Função que recebe nome e quatidade de gols de um jogador             #
#                                       e mostra a ficha dele                            #
##########################################################################################

import string


def ficha(nome, gols=0):
    """
    -> Mostra a ficha de um jogador.
    :param nome: o nome do jogador, opcional.
    :param gols: quantidade de gols que o jogador fez no campeonato.
    :return: sem retorno.
    """
    nome = '<desconhecido>' if len(nome) == 0 else nome
    gols = 0 if len(gols) == 0 or gols != string.digits else gols
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

print('-' * 30)
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))
ficha(nome, gols)