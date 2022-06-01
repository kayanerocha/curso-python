dados = list()
pessoas = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    while True:
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua in 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')

menor_peso = pessoas[0][1]
maior_peso = pessoas[0][1]

for p in pessoas:
    if p[1] < menor_peso:
        menor_peso = p[1]

    if p[1] > maior_peso:
        maior_peso = p[1]

print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')

print()

print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
