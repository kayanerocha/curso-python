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

def linha(tamanho):
    print('-' * (tamanho + 20))

def titulo(msg):
    tamanho = len(msg)
    linha(tamanho)
    print(' ' * 10 + msg)
    linha(tamanho)


def resumo(valor, porcen_aumenta, porcen_diminui):
    msg = 'RESUMO DO VALOR'
    titulo(msg)
    
    print(f'Preço analisado:\t {moeda(valor)}')
    print(f'Dobro do preço:\t\t {dobro(valor, True)}')
    print(f'Metade do preço:\t {metade(valor, True)}')
    print(f'{porcen_aumenta}% de aumento:\t\t {aumentar(valor, porcen_aumenta, True)}')
    print(f'{porcen_diminui}% de redução:\t\t {diminuir(valor, porcen_diminui, True)}')
    
    linha(len(msg))