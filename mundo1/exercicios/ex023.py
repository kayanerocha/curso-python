numero = int(input('\033[1mNúmero de 0 a 9999:\033[m '))

milhar = numero // 1000  # numero // 1000 % 10
centena = (numero % 1000) // 100  # numero // 100 % 10
dezena = (numero % 100) // 10  # numero // 10 % 10
unidade = (numero % 10)  # numero // 1 % 10

print('{}unidade: {}{}{}'.format('\033[31m', '\033[32m', unidade, '\033[m'))
print('{}dezena: {}{}{}'.format('\033[31m', '\033[33m', dezena, '\033[m'))
print('{}centena: {}{}{}'.format('\033[31m', '\033[34m', centena, '\033[m'))
print('{}milhar: {}{}{}'.format('\033[31m', '\033[35m', milhar, '\033[m'))