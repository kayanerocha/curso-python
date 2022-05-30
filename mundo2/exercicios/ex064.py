numero = 0
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Número: '))
    if numero != 999:
        cont += 1
        soma += numero
print('Foram digitados {} números e a soma deles é {}'.format(cont, soma))