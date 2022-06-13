##########################################################################################
#                       Função que recebe um texto como parâmetro e mostre               #
#                               uma mensaem com tamanho adaptável                        #
##########################################################################################

def escreva(mensagem):
    print('~' * len(mensagem))
    print(mensagem)
    print('~' * len(mensagem))

escreva('   Gustavo Guanabara   ')
escreva('  Curso de Python no YouTube  ')
escreva('  CeV  ')