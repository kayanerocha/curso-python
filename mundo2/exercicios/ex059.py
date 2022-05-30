opcao = 4
retorno = 0

while opcao == 4:
    valor1 = float(input('Valor 1: '))
    valor2 = float(input('Valor 2: '))
    opcao = 0

    while opcao != 5 and opcao != 4:
        print('''Escolha uma opcão:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
        opcao = int(input('Opção: '))

        if opcao == 1:
            print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
        elif opcao == 2:
            print('{} * {} = {}'.format(valor1, valor2, valor1 * valor2))
        elif opcao == 3:
            if valor1 > valor2:
                maior = valor1
            else:
                maior = valor2
            print('{} é o maior'.format(maior))
        elif opcao < 1 or opcao > 5:
            print('Opção inválida.')
print('Finalizando...')