primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

i = 1
while i < 11:
    print(primeiro_termo, end=' -> ' if i < 10 else '')
    primeiro_termo += razao
    i += 1