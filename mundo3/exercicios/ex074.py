from random import randint

numeros = ()
for i in range(0, 5):
    n = randint(0, 100)
    numeros += (n,)

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')

'''
for p, m in enumerate(numeros):
    if p == 0:
        maior = m
        menor = m
    else:
        if m > maior:
            maior = m
        if m < menor:
            menor = m
'''
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')