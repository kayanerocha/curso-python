##################################################################################
#                                 Funções (Parte 1)                              #
##################################################################################

# Rotina: programas que fazem coisas constantemente, funções. Evita repetição de código, otimiza
#   - print()
#   - len()
#   - input()
#   - int()
#   - float()

def mensagem(mensagem):
    print('-' * 30)
    print(mensagem)
    print('-' * 30)

# mensagem('      SISTEMA DE ALUNOS   ')

# ------------------------------------------------------------------------------

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-' * 30)


# Programa principal
# soma(4, 5)
# soma(a=8, b=9)
# soma(b=2, a=1)

# ----------------------------- EMPACOTAMENTO ------------------------------
# Empacota vários parâmetros de uma função

# * significa desempacotar todos os parâmetros que estão em uma tupla
def contador(*num):
    for valor in num:
        print(valor, end=' ')
    print('FIM!')

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# ---------------------------------------------------------------------------

def dobra(valores):
    posicao = 0
    while posicao < len(valores):
        valores[posicao] *= 2
        posicao += 1

    print(f'Valores dobrados: {valores}')

valores = [7, 2, 5, 0, 4]
print(f'Valores iniciais: {valores}')
dobra(valores)


