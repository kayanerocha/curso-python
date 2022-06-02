matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0
# preenche a matriz por linha
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        matriz[linha].insert(coluna, valor)

        # soma os valores pares
        if valor % 2 == 0:
            soma_pares += valor

        # soma os valores da terceira coluna
        if coluna == 2:
            soma_terceira_coluna += valor
        
        # pega o maior valor da segunda linha
        if linha == 1 and valor > maior_segunda_linha:
            maior_segunda_linha = valor

# imprime a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end='\n' if coluna == 2 else ' ')

print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')
