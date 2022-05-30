from datetime import date

atingiram = 0
nao_atingiram = 0
for i in range(1, 8):
    ano = int(input('Ano de nascimento da pessoa {}: '.format(i)))
    idade = date.today().year - ano
    if idade < 18:
        nao_atingiram += 1
    else:
        atingiram += 1
print('{} pessoas não atingiram a maior idade e {} pessoas atingiram.'.format(nao_atingiram, atingiram))