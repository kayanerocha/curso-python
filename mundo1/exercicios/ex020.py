import random

aluno1 = input('\033[36mDigite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4:\033[m ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('\033[7mA ordem de apresentação será:\033[m ')
print('{}{}{}'.format('\033[31m', lista, '\033[m'))

# i = 1
# while i <= 4:
#    sorteado = random.choice(lista)
#    lista.remove(sorteado)
#    print('{} - {}'.format(i, sorteado))
#    i += 1

