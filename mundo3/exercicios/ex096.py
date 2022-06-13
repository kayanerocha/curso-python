##########################################################################################
#           Função chamada área que recebe as imensões de um terreno retangular (largura #
#                       e comprimento) e mostre a área do terreno                        #
##########################################################################################

def titulo():
    print('Controle de Terrenos')
    print('-' * 25)

def solicita_dados():
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))

    return [largura, comprimento]

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {a:.1f}m².')


# Programa principal
titulo()
dados = solicita_dados()
area(dados[0], dados[1])
