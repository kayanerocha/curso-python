##########################################################################################
#               Guarda nome, média e situação de um aluno em um dicionário               #
##########################################################################################

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'

print('-=' * 30)
for key, value in aluno.items():
    print(f'   - {key} é igual a {value}')