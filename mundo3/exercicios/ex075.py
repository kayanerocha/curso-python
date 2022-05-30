valores = ()
while True:
    valor = int(input('Informe um valor: '))
    valores += (valor, )
    if len(valores) == 4:
        break
print(f'Você digitou os valores {valores}')
print(f'O 9 apareceu {valores.count(9)} vezes')
print(f'O primeiro 3 está na {valores.index(3) + 1}ª posição')
print('Os valores pares são: ', end='')
for v in valores:
    if v % 2 == 0:
        print(f'{v}', end=' ')