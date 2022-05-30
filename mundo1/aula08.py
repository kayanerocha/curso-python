import math
import random
import emoji
# Bibliotecas
    # import biblioteca
    # from math import funcionalidade

# math
    # ceil: arredonda o numero para frente
    # floor: arredonda o numero para tras
    # trunc: corta os números da virgula para frente sem arredondar
    # pow: potencia
    # sqrt: raiz quadrada
    # factorial: calcula o fatorial

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.trunc(raiz)))

n1 = random.random()
n2 = random.randint(1, 10)
print(n1, n2)

print(emoji.emojize('Olá, mundo :sunglasses:'))
print(emoji.emojize('Olá, mundo :earth_americas:'))
