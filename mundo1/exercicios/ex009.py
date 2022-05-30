cores = {'limpa': '\033[m',
         'negrito': '\033[1m',
         'negrito-verde': '\033[1;32m',
         'lilas': '\033[35m'}
n = int(input('{}Número da tabuada desejada:{} '.format(cores['negrito'], cores['limpa'])))
i = 0
while i < 10:
    print('{}{} * {} ={} {}{}{}'.format(cores['negrito-verde'], n, i, cores['limpa'], cores['lilas'], n * i,
                                        cores['limpa']))
    i += 1
