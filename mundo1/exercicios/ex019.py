import random

form = {'limpa': '\033[m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'lilas': '\033[35m'}

aluno1 = input('{}Digite o nome do aluno 1:{} '.format(form['vermelho'], form['limpa']))
aluno2 = input('{}Digite o nome do aluno 2:{} '.format(form['verde'], form['limpa']))
aluno3 = input('{}Digite o nome do aluno 3:{} '.format(form['amarelo'], form['limpa']))
aluno4 = input('{}Digite o nome do aluno 4:{} '.format(form['azul'], form['limpa']))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('{}O aluno escolhido foi {}{}'.format(form['lilas'], escolhido, form['limpa']))
