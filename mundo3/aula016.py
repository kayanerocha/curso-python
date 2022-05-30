# --------------------------------------------------#
#                    #16 - Tuplas                   #
# --------------------------------------------------#

"""
- variável que guarda vários valores
- string é uma variável composta do tipo lista
- cada valor é acessado pelo índice
    - tupla[0]: o primeiro item
    - tupla[0:2]: do primeiro até o segundo item
    - tupla[1:]: do segundo até o último item
    - tupla[-1]: último item
- len(tupla): quantidade de itens na tupla
- for t in tupla:
    print(t)  # printa cada elemento da tupla
- elas são imutáveis
"""

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # pode ser sem parenteses também

'''
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(len(lanche))
'''

# lanche[1] = 'Refrigerante'  # dar erro por ser imutável


for comida in lanche:
    print(f'Eu vou comer {comida}')


'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
'''

'''
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
'''

'''
print(sorted(lanche))  # coloca em ordem sem alterar a tupla
print(lanche)
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # junta as duas
d = b + a
print(c)
print(d)
print(len(c))
print(c.count(5))  # quantas vez o 5 aparece
print(c.index(8))  # posição do 8
print(c.index(5))  # se tiver mais de um mostra o primeiro
print(c.index(5, 2))  # posição de 5 a partir da posição 2
'''

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
# del pessoa[0]  # não funciona
del pessoa  # apaga a pessoa