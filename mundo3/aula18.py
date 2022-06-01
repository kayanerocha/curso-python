##################################################################################
#                      Variávies Compostas (Listas)                              #
##################################################################################

dados = list()
dados.append('Pedro')
dados.append(25)
# print(f'Dados: {dados}')

# Lista dentro de lista
pessoas = list()
pessoas.append(dados[:]) # adiciona uma cópia da lista dados
# print(f'Pessoas: {pessoas}')
# print(f'Nome da primeira pessoa: {pessoas[0][0]}')

# -------------------------------------------------------------------------

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
# print(f'1: {galera}')

# se colocar sem [:] os dados de gustavo serão substituídos pelos de maria
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
# print(f'2: {galera}')

# -------------------------------------------------------------------------

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# print(f'Galera: {galera}')
# print(f'Primeira pessoa: {galera[0]}')
# print(f'Nome da primeira pessoa: {galera[0][0]}')

# for p in galera:
#    print(f'{p[0]} tem {p[1]} anos')

# -------------------------------------------------------------------------

galera = list()
dado = list()
total_maior = total_menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} maiores e {total_menor} menores de idade.')