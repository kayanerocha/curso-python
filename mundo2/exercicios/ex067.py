limite = resultado = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    while limite < 10:
        resultado = valor * limite
        limite += 1
        print(f'{valor} * {limite} = {resultado}')
    limite = 0