total = cont = preco_alto = menor_preco = 0
nome_barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'NS':
            break

    total += preco
    cont += 1
    if preco > 1000:
        preco_alto += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        nome_barato = nome

    if resposta not in 'Ss':
        break
print(f'O total gasto na compra foi de R${total:.2f}. \n{preco_alto} produtos custam mais de R$1000. \n'
      f'{nome_barato} é o produto mais barato.')