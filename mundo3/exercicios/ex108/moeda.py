def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

def aumentar(valor, porcentagem, formata=False):
    if formata:
        novo_valor = moeda(valor + ((valor * porcentagem) / 100))
    else:
        novo_valor = valor + ((valor * porcentagem) / 100)
    return novo_valor

def diminuir(valor, porcentagem, formata=False):
    if formata:
        novo_valor = moeda(valor - ((valor * porcentagem) / 100))
    else:
        novo_valor = valor - ((valor * porcentagem) / 100)
    return novo_valor

def dobro(valor, formata=False):
    if formata:
        novo_valor = moeda(valor * 2) 
    else:
        novo_valor = valor * 2
    return novo_valor

def metade(valor, formata=False):
    if formata:
        novo_valor = moeda(valor / 2)
    else:
        novo_valor = valor / 2
    return novo_valor


