##################################################################################
#                       Tratamento de Erros e Exceções                           #
##################################################################################

# Erro de sintaxe: primt(x)
# Erro semântico: print(x) se x não tiver sido definido

# Dispara a exceção NameError
# print(x)

# Se não informar um inteiro dispara a exceção ValueError
# n = int(input('Número: '))
# print(f'Você digitou o número {n}')

# Se o denominador for 0 dispara a exceção ZeroDivisionError
# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}')

# Exceção TypeError: r = 2 / '2'

# Exceção IndexError, se for dicionário é KeyError
from typing import Type


lst = [2, 6, 4]
# print(lst[3]) # 3 não existe na lista

# Exceção ModuleNotFoundError: se importar um módulo que não existe

# Toda exceção é filha da classe Exception

# Trata as exeções:
try: # tente executar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# Pode ter vários except, se não der certo
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero!')
except KeyboardInterrupt:
     print(f'O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: # se der certo (opcional)
    print(f'O resultado é {r:.1f}')
finally: # aconcete independente se deu certo ou não (opcional)
    print('Volte sempre! Muito obrigado!')
