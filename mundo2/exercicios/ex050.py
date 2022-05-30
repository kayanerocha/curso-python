soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input('Número {}: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Voçe informou {} números pares e a soma foi {}'.format(cont, soma))