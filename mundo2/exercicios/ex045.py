import random

alguem_ganhou = False

while not alguem_ganhou:
    minha_jogada = str(input('Pedra, papel ou tesoura? ')).strip().upper()

    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    jogada_comp = random.choice(opcoes)
    print('Jogada do computador: {}'.format(jogada_comp))

    if minha_jogada == opcoes[2] and jogada_comp == opcoes[1]:
        print('Eu ganhei.')
        alguem_ganhou = True
    elif minha_jogada == opcoes[0] and jogada_comp == opcoes[2]:
        print('Eu ganhei.')
        alguem_ganhou = True
    elif minha_jogada == opcoes[1] and jogada_comp == opcoes[0]:
        print('Eu ganhei.')
        alguem_ganhou = True
    elif minha_jogada == jogada_comp:
        print('Empatou, jogue novamente.')
    else:
        print('O computador ganhou.')
        alguem_ganhou = True