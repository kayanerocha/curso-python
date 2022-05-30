# --------------------------------------------------#
#            #12 - Condições Aninhadas              #
# --------------------------------------------------#

nome = str(input('Qual é o seu nome? '))
if nome == 'Kayane':
    print('Que belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é normal.')
print('Tenha um nom dia, {}!'.format(nome))