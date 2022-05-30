numero = int(input('\033[1mNúmero:\033[m '))
if numero % 2 == 0:
    print('\033[31mNúmero par.\033[m')
else:
    print('\033[32mNúmero ímpar.\033[m')