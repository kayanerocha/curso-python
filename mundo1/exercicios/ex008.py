m = float(input('\033[1mValor em metros:\033[m '))
cm = m * 100
mm = m * 1000
cores = {'limpa': '\033[m',
         'inverte': '\033[1;7m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m'}
print('{}{}m{} vale {}{}cm{} e {}{}mm{}'.format(cores['inverte'], m, cores['limpa'], cores['vermelho'], cm,
                                                cores['limpa'], cores['azul'], mm, cores['limpa']))
