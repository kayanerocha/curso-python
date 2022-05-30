menor = 0
valores = []
for i in range(0, 5):
    valor = int(input('Valor: '))
    if len(valores) == 0:
        valores.append(valor)
        menor = valor
    else:
        for p, v in enumerate(valores):
            if valor < v:
                menor = valor
                valores.insert(p, valor)
                break
            else:
                valores.append(valor)
                break
print(valores)