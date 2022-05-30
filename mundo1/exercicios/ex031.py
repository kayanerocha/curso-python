distancia = float(input('\033[1;4mDistância em Km:\033[m '))
'''
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
'''
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('O preço da passagem é {}R${:.2f}{}'.format('\033[33m', preco, '\033[m'))