colocados = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Athetico-PR',
             'Internacional', 'Fluminense', 'América-MG', 'Atlético-GO', 'Cuiabá', 'Ceará SC', 'São Paulo',
             'Juventude', 'Santos', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print('Os 5 primeiro colocados são:')
for p in range(0, len(colocados) - 15):
    print(f'{p + 1} - {colocados[p]}')

print('\nO últimos 4 colocados da tabela são: ')
for u in range(0, -(len(colocados) - 16), -1):
    print(f'{(u + 1) + (len(colocados) - 1) } - {colocados[u - 1]}')

print('\nOutra forma: ')
for u2 in range(-4, 0):
    print(f'{u2 * (-1)} - {colocados[u2]}')

print('\nOs times em ordem alfabética: ')
for o in sorted(colocados):
    print(o)

for p, c in enumerate(colocados):
    if c == 'Chapecoense':
        print(f'\nO posição da Chapecoense é {p + 1}')