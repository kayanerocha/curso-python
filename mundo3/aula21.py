##################################################################################
#                                 Funções (Parte 2)                              #
##################################################################################

# --------------------------------- INTERACTIVE HELP -----------------------------

# Busca o manual de qualquer comando
    # Para acessar no terminal: python -> help()
    # Exemplos de comandos: print, len, input, datetime
    # Para sair: quit

# Fora do terminal:
# help(print)
# print('-' * 30)
# print(input.__doc__)

# --------------------------------- DOCSTRINGS -----------------------------------
# Documenta as funções de um programa para que essa doc fique acessível pelo help

def contador(i, f, p):
    # Faz o manual logo abaixo do comando def
    """
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
        Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

# contador(2, 10, 2)
# help(contador)

# --------------------------------- ARGUMENTOS OPCIONAIS -----------------------------
# deixa c como opcional, pode deixar todos opcionais
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVideo
    """
    s = a + b + c
    print(f'A soma vale {s}')

# somar(3, 2, 5)
# somar(8, 4)
# somar()

# --------------------------------- ESCOPO DE VARIÁVEIS -----------------------------
# Onde uma variável existe e onde deixa de existir
def teste():
    # Mesmo n estando fora da função ela vai existir em todo o programa, no escopo global
    print(f'Na função teste, n vale {n}')

    # Existe apenas dentro da função, no escopo local
    x = 8
    print(f'Na função teste, x vale {x}')

# Programa Principal
n = 2
# print(f'No programa principal, n vale {n}')
# teste()

def testandoEscopo(b):
    global a # Para usar a variável de escopo global e não criar um nova variável de escopo local 
    a = 8 # Cria uma nova variável de escopo local se não usar global a
    b += 4 # Adiciona 4 ao valor passado
    c = 2

    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

# Programa Principal
a = 5
# print(f'A fora antes da função vale {a}')
# testandoEscopo(a) # B recebe o valor global de A
# print(f'A fora depois da função vale {a}')

# --------------------------------- RETORNO DE VALORES -----------------------------
# As funções podem retornar ou não um valor

def somarComReturn(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somarComReturn(3, 2, 5)
r2 = somarComReturn(2, 2)
r3 = somarComReturn(6)
# print(f'As somas valem {r1}, {r2} e {r3}')

# -------------------------------------- FATORIAL -----------------------------------
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')