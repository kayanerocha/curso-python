peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / pow(altura, 2)
print('Seu IMC é de {:.2f}, você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 <= imc < 25:
    print('no peso ideal.')
elif 25 <= imc < 30:
    print('com sobrepeso')
elif 30 <= imc <= 40:
    print('com obesidade')
else:
    print('com obesidade mórbida.')