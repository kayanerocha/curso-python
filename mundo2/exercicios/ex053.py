frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = ''
# tamanho = len(junto)
inverso = junto[::-1]
'''
for letra in range(tamanho - 1, -1, -1):
    inverso += junto[letra]
'''
print('O inverso de {} é {}'.format(junto, inverso))

if junto == inverso:
    print('A frase é palíndromo.')
else:
    print('A frase não é palíndromo.')

