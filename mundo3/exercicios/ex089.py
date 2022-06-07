notas = list()
alunos = list()

# [[nome[nota1, nota2]], []]

while True:
    nome = str(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append([nome, notas[:]])
    notas.clear()
    
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar in 'N':
        break

print('-=' * 30)
print(f'{"N°":<2} {"NOME":<15} {"MÉDIA":>8}')
print('-' * 30)

for posicao, aluno in enumerate(alunos):
    print(f'{posicao:<2} {aluno[0]:<15} {(aluno[1][0] + aluno[1][1]) / 2:8.1f}')

print('-' * 40)
while True:
    posicao_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if posicao_aluno == 999:
        break
    else:
        print(f'Notas de {alunos[posicao_aluno][0]} são {alunos[posicao_aluno][1]}')
        print('-' * 40)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
    
