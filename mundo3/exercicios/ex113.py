##########################################################################################
#        Funções que leiam números inteiros e reais usando tratamento de exceções        #
##########################################################################################

def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            inteiro = 0
            break
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    return inteiro

def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            real = 0
            break
        except:
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
        else:
            break
    return real
        

num_inteiro = leiaInt('Digite um Inteiro: ')
num_real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {num_inteiro} e o real foi {num_real}')