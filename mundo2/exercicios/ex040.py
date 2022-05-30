nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print('Sua média é {:.2f}'.format(media))
if media < 5.0:
    print('Reprovado.')
elif 5.0 <= media < 7.0:
    print('Recuperação.')
else:
    print('Aprovado.')