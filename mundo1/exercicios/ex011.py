formata = {'limpa': '\033[m',
           'negrito_invertido': '\033[1;7m',
           'azul': '\033[34m',
           'ciano': '\033[36m'}
l = float(input('{}Digite a largura da parede em metros:{} '.format(formata['negrito_invertido'], formata['limpa'])))
a = float(input('{}Digite a altura da parede em metros:{} '.format(formata['negrito_invertido'], formata['limpa'])))
area = l * a
print('A área da parede é {}{}m²{} e a quantidade de tinta que será utlizada é {}{}L{}'.format(formata['azul'], area,
                                                                                               formata['limpa'],
                                                                                               formata['ciano'],
                                                                                               area / 2,
                                                                                               formata['limpa']))
