##########################################################################################
#                   Função que recebe o para calcular o fatorial e se é                  #
#                        para mostrar na tela o processo de cálculo                      #
##########################################################################################

def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do Fatorial de um número.
    """
    fat = 1
    for c in range(numero, 0, -1):
        fat *= c
        if show:
            print(f'{c}', end=' x ' if c > 1 else f' = ')     
    return fat

print('-' * 30)
print(fatorial(5))
help(fatorial)
