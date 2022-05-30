n1 = float(input('\033[1mDigite a primeira nota:\033[m '))
n2 = float(input('\033[1mDigite a segunda nota:\033[m '))
m = (n1 + n2) / 2
print('A média do aluno é {}{}{}'.format('\033[1;4m', m, '\033[m'))