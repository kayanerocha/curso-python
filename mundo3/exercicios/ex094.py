##########################################################################################
#           Guarda dicionários em uma lista e analisa os dados de pessoas                #
##########################################################################################

dados = dict()
pessoas = list()
idades = list()
while True:
    dados['nome'] = str(input('Nome: '))

    while True:
        dados['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
        if dados['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apena M ou F.')

    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    idades.append(dados['idade'])

    while True:
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if continuar in 'N':
        break

print('-=' * 30)
print(f'- Foram cadastradas {len(pessoas)} pessoas.')
print(f'- A média de idade do grupo é {sum(idades) / len(pessoas):.2f} anos.')

print(f'- Mulheres da lista: ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] in 'F':
        print(pessoa['nome'], end=' ')
print()

print('- Pessoas com idade acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > sum(idades) / len(pessoas):
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<< ENCERRADO >>')