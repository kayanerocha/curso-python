n1 = int(input('\033[1;34mNúmero 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3:\033[m '))
# verificando que é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificanod quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('{}O menor é {}{}'.format('\033[32m', menor, '\033[m'))
print('{}O maior é {}{}'.format('\033[31m', maior, '\033[m'))