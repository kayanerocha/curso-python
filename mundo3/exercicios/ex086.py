matriz = [[], [], []]
# preenche a matriz por linha
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        matriz[linha].insert(coluna, valor)

# imprime a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end='\n' if coluna == 2 else ' ')

