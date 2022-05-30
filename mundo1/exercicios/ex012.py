preco = float(input('\033[1;4mDigite o preço do produto R$\033[m'))
print('{}O novo preço do produto é {}R${}{}'.format('\033[1m', '\033[41m', preco - (preco * 5) / 100, '\033[m'))
