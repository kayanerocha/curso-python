nome_completo = str(input('\033[31mNome completo:\033[m ')).strip()
nome = nome_completo.split()
print('\033[32mprimeiro: {}\033[m'.format(nome[0]))
print('\033[32múltimo: {}\033[m'.format(nome[len(nome) - 1]))
