primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for i in range(1, 11):
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
print('ACABOU')