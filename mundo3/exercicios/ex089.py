notas = list()
alunos = list()

# [[nome[nota1, nota2]], []]

while True:
    nome = str(input('Nome: '))
    notas.append(int(input('Nota 1: ')))
    notas.append(int(input('Nota 2: ')))
    alunos.append([nome, notas[:]])
    notas.clear()
    
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print(alunos)
# calcula e imprime a média de cada aluno
# for aluno in alunos:
#     media = (aluno[1] + aluno[2]) / 2
#     print(f'{aluno[0]} tem a média de {media:.1f} pontos.')
