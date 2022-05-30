expressao = str(input('Digite a expressão: ')).strip()
paren_abertos = expressao.count('(')
paren_fechados = expressao.count(')')
'''
if paren_abertos == paren_fechados:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
'''

abertos = fechados = 0
certo = False
for c in expressao:
    if c in '(':
        abertos += 1
    elif c in ')':
        fechados += 1
        if fechados > abertos:
            break
if abertos > fechados:
    certo = False
elif abertos == fechados:
    certo = True

if certo:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')