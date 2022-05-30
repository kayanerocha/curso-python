import random
from time import sleep

f = {'limpa': '\033[m',
     'verm': '\033[31m',
     'verde': '\033[32m',
     'neg-azul': '\033[1;34m',
     'neg-amarelo': '\033[1;33m',
     'neg-lilas': '\033[1;35m'}

numero = random.randint(0, 5)
print('{}{}'.format(f['neg-azul'], '-=' * 30))
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('{}{}'.format('-=-' * 20, f['limpa']))
chute = int(input('{}Em que número eu pensei?{} '.format(f['neg-lilas'], f['limpa'])))
print('{}PROCESSANDO...{}'.format(f['neg-amarelo'], f['limpa']))
sleep(2)  # segundos para rodar os códigos seguintes
if chute == numero:
    print('{}PARABÉNS! Você conseguiu me vencer!{}'.format(f['verde'], f['limpa']))
else:
    print('{}GANHEI! Eu pensei no número {} e não no {}!{}'.format(f['verm'], numero, chute, f['limpa']))