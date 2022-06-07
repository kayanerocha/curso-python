##################################################################################
#                                 Dicionários                                    #
##################################################################################

dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados)

# adiciona um novo elemento
dados['sexo'] = 'M'
print(dados)

# remove um elemento
del dados['idade']
print(dados)

# retorna os valores
print(dados.values())

# retorna as chaves
print(dados.keys())

# retorna os itens (chaves e valores)
print(dados.items())

# imprimindo chaves e valores
for key, value in dados.items():
    print(f'{key}: {value}')

# adicionando o dicionário em uma lista
alunos = list()
alunos.append(dados)
print(alunos)

# ----------------------------------------------------------------------

print('-' * 50)

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'Nome: {pessoas["nome"]}')
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# altera o nome
pessoas['nome'] = 'Leandro'

print('Chaves:')
for key in pessoas.keys():
    print(key)

print('Valores:')
for value in pessoas.values():
    print(value)

print('Itens:')
for key, value in pessoas.items():
    print(f'{key} = {value}')

# -------------------------------------------------------------------

print('-' * 50)

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['uf'])

# --------------------------------------------------------------------

print('-' * 50)

estados = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    estados.append(estado.copy()) # adiciona uma cópia do dicionário na lista

for e in estados:
    # for key, value in e.items():
    #     print(f'O campo {key} tem valor {value}')

    for v in e.values():
        print(v, end=' ')
    print()
