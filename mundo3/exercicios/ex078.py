valores = []
for i in range(0, 5):
    valor = int(input('Digite um valor para a posição {}: '.format(i)))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

print(f'O maior valor foi {maior} nas posições', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f' {p}...', end='')

print(f'\nO menor valor foi {menor} nas posições', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f' {p}...', end='')