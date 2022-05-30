n = int(input('\033[1mDigite um número inteiro: \033[m'))
print('O antecessor do número {}{}{} é {}{}{} e o sucessor é {}{}{}'.format('\033[1;31m', n, '\033[m', '\033[1;32m',
                                                                            n - 1, '\033[m', '\033[1;32m', n + 1,
                                                                            '\033[m'))
