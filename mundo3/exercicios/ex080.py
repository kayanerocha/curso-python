menor = 0
posicao_menor = 0
valores = []
is_menor = False

for i in range(0, 5):
    valor = int(input('Digite um Valor: '))

    if len(valores) == 0:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for p, v in enumerate(valores):
            if valor < v:
                is_menor = True
                menor = valor
                posicao_menor = p
                break
            else:
                is_menor = False
        if is_menor:
            valores.insert(posicao_menor, menor)
            print(f'Adicionado na posição {posicao_menor} da lista...')
        else:
            valores.append(valor)
            print('Adicionado ao final da lista...')

print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')



# Solução do Guanabara

lista = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
