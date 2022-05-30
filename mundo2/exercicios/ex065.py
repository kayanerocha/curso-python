condicao = 'S'
cont = soma = maior = menor = 0
while condicao != 'N':
    numero = int(input('Número: '))
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    condicao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('Você digitou {} números e a média foi {}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))