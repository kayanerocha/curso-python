from datetime import date, datetime

trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['ano_nascimento'] = int(input('Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - trabalhador['ano_nascimento']
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratacao'] = int(input('Ano de Contração: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    
    anos_contribuidos = datetime.now().year - trabalhador['ano_contratacao'] # anos de contribuição desde a contratação
    anos_restantes = 35 - anos_contribuidos # anos que restam para se aposentar
    trabalhador['idade_aposentadoria'] = trabalhador['idade'] + anos_restantes

print('-=' * 30)
for key, value in trabalhador.items():
    print(f'{key} tem o valor {value}')