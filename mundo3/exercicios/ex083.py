expressao = str(input('Digite a expressão: ')).strip()

abertos = fechados = 0
for c in expressao:
    if c in '(':
        abertos += 1
    elif c in ')':
        fechados += 1
        if fechados > abertos:
            break

if abertos == fechados:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')