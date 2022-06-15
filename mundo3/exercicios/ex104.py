##########################################################################################
#                   Função que valida se a entrada do usuário é um int                   #
##########################################################################################

def leiaInt(mensagem):
    """
    -> Valida se a entada é um inteiro.
    :param mensagem: mensagem que solicita a entrada.
    :return: o número informado pelo usuário.
    """
    while True:   
        numero = str(input(mensagem)).strip()
        if numero.isnumeric():
            numero = int(numero)
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return numero

numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')