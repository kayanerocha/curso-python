# --------------------------------------------------#
#             #16 - Listas (Parte 1)                #
# --------------------------------------------------#

"""
- lista = []
- podem ser modificadas
- lista.append('item') adiciona um item no final
- lista.insert(0, 'item') adiciona um item na posição 0
- del lista[indice] remove o item pelo indice
- lista.pop(3) remove o item pelo indice, se não colocar o indice remove o último
- lista.remove('item') remove o primeiro item por ele
- valores = list(range(4, 11)) cria uma lista com os números de 4 a 10
- valores.sort() coloca os iten em ordem
- valores.sort(reverse=True) coloca os iten em ordem na ordem reversa
"""


num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.insert(0, 2)
print(num)
num.sort()
print(num)
'''
num.sort(reverse=True)
print(num)

print(len(num))

num.pop()
print(num)

num.remove(2)  # remover apenas o primeiro
print(num)
'''

"""
valores = list()
'''
valores.append(5)
valores.append(9)
valores.append(4)
'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for valor in valores:
    print(f'{valor}...')

for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
"""

"""
a = [2, 3, 4, 7]
b = a  # faz uma ligação
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('-' * 20)

b[2] = 8  # altera nas duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('-' * 20)

c = a[:]  # cria uma cópia
c[2] = 9  # altera somente em b
print(f'Lista A: {a}')
print(f'Lista C: {c}')
"""