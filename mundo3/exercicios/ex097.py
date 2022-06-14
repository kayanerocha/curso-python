##########################################################################################
#                       Função que recebe um texto como parâmetro e mostre               #
#                               uma mensaem com tamanho adaptável                        #
##########################################################################################

def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')