maiores = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo? [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break

    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    if resposta == 'N':
        break
print(f'{maiores} pessoas tem mais de 18 anos, {homens} homens foram cadastrados e {mulheres} mulheres tem menos de 20 anos.')