forma = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'lilas': '\033[35m',
         'ciano': '\033[36m',
         'vermelho': '\033[31m'}

nome = str(input('{}Nome completo:{} '.format(forma['amarelo'], forma['limpa']))).strip()
print('{}nome em maiusculo:{} {}{}{}'.format(forma['amarelo'], forma['limpa'], forma['azul'], nome.upper(),
                                             forma['limpa']))
print('{}nome em minúsculo:{} {}{}{}'.format(forma['amarelo'], forma['limpa'], forma['lilas'], nome.lower(),
                                             forma['limpa']))
print('{}o nome completo tem {}{} {}letras{}'.format(forma['amarelo'], forma['ciano'], len(nome.replace(' ', '')),
                                                     forma['amarelo'], forma['limpa']))
# print('o nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
nome_separado = nome.split()
print('{}o primeiro nome tem {}{} {}letras{}'.format(forma['amarelo'], forma['vermelho'], len(nome_separado[0]),
                                                        forma['amarelo'], forma['limpa']))
# print('o primeiro nome tem {} letras'.format(nome.find(' ')))
