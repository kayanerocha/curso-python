produtos = ()
for i in range(1, 3):
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    produtos += (nome, preco, )

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<25}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')