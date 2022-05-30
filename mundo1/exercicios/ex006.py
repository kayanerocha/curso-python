n = int(input('\033[1;4mDigite um número:\033[m '))
print('O dobro do número {}{}{} é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{}{}'.format('\033[34:40m', n,
                                                                                               '\033[m', '\033[30;44m',
                                                                                               n * 2, '\033[m',
                                                                                               '\033[30;44m', n * 3,
                                                                                               '\033[m', '\033[30;44m',
                                                                                               n ** (1 / 2), '\033[m'))
