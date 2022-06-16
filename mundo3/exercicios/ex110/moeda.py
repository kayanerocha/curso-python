from ex107.moeda import aumentar, diminuir, dobro, metade, moeda

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
    print(f'{porcen_aumenta}% de aumento:\t\t {aumentar(valor, porcen_aumenta, True):<15}')
    print(f'{porcen_diminui}% de redução:\t\t {diminuir(valor, porcen_diminui, True):<15}')
    
    linha(len(msg))