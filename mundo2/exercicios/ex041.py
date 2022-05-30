from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Categoria: ', end='')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')