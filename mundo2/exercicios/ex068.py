from random import randint
valor_jogador = computador = total = 0
resultado = par_impar = ''
cont = 0
while True:
    valor_jogador = int(input('Diga um valor: '))
    while par_impar not in 'PI':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    total = valor_jogador + computador
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'Você jogou {valor_jogador} e o computador {computador}. Total de {total} DEU {resultado}')
    if resultado[0] == par_impar:
        cont += 1
        print('Você VENCEU! \nVamos jogar novamente...')
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {cont} vezes.')