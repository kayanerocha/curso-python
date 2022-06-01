numeros = []
while True:
    n = int(input('Número: '))
    numeros.append(n)
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
    if resposta in 'N':
        break

print(f'Você digitou {len(numeros)} elementos.')

numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print(f'O valor 5 faz parte da lista na posição {numeros.index(5)}!')
else:
    print('O valor 5 não foi encontrado na lista!')