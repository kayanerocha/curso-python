numeros = [[], []]
for c in range(0, 7):
    numero = int(input('Número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f'Números pares: {sorted(numeros[0])}')
print(f'Número ímpares: {sorted(numeros[1])}')