# from ex107.moeda import metade, dobro, diminuir, aumentar # um não pode importar o outro

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')


