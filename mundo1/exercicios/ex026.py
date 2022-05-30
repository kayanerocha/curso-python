frase = str(input('{}Frase:{} '.format('\033[34m', '\033[m'))).strip().upper()
frase_formatada = ' '.join(frase.split())

print('{}A letra A aparece {}{}{} {}vezes{}'.format('\033[34m', '\033[4;35m', frase.count('A'), '\033[m',
                                                    '\033[34m', '\033[m'))
print('{}A letra A apareceu pela primeira vez na posição {}{}{}'.format('\033[34m', '\033[4;36m', frase.find('A')+1,
                                                                        '\033[m'))
print('{}A letra A apareceu pela última vez na posição {}{}{}'.format('\033[34m', '\033[4;31m', frase_formatada.rfind('A')+1,
                                                                      '\033[m'))