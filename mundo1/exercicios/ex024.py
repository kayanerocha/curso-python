cidade = str(input('\033[1;4;36mCidade:\033[m ')).strip()
divide = cidade.split()
print('{}{}{}'.format('\033[31m', 'SANTO' in divide[0].upper(), '\033[m'))
# print(cidade[:5].upper() == 'SANTO')
