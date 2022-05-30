from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento que será em {}.'.format(18 - idade, ano_nasc + 18))
elif idade == 18:
    print('É hora de se alistar.')
else:
    print('Você já deveria ter se alistado há {} anos, seu alistamento foi em {}.'.format(idade - 18, ano_nasc + 18))