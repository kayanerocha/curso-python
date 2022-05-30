d = float(input('\033[1;4mDigite a sua quantidade de dinheiro\033[m R$'))
print('Você pode comprar {}US${}{}'.format('\033[1;4;34m', round((d / 3.27), 2), '\033[m'))
