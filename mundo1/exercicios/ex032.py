from datetime import date
ano = int(input('\033[36mQual ano quer analisar? Coloque 0 para analisar o ano atual:\033[m '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('\033[34mO ano {} é bissexto.\033[m'.format(ano))
else:
    print('\033[35mO ano {} não é bissexto.\033[m'.format(ano))