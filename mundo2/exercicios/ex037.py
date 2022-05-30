numero = int(input('Número inteiro: '))
print('''Escolha uma base para conversão:
1 - Binário
2 - Octal
3 - Hexadecimal''')
opcao = int(input('Opção: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecima é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')