primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

i = 1
limite = 11
termos = -1

while termos != 0:
    while i < limite:
        print(primeiro_termo, end=' -> ' if i < limite - 1 else '')
        primeiro_termo += razao
        i += 1

    termos = int(input('\nQuer mostras mais termos? Informe a quantidade: '))
    limite += termos
print('Progressão finalizada com {} termos mostrados.'.format(limite))