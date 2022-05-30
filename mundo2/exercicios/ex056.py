soma = 0
mulheres = 0
nome_mais_velho = ''
idade_mais_velho = 0
for i in range(1, 5):
    nome = str(input('Nome da pessoa {}: '.format(i)))
    idade = int(input('Idade da pessoa {}: '.format(i)))
    sexo = str(input('Sexo da pessoa {} (M ou F): '.format(i))).strip()
    soma += idade
    if i == 1 and sexo in 'Mn':
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Mn' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if idade < 20 and sexo in 'Ff':
        mulheres += 1
print('A média de idade do grupo é de {:.1f} anos'.format(soma / 4))
print('{} é o homem mais velho com {} anos'.format(nome_mais_velho, idade_mais_velho))
print('Têm {} mulheres com menos de 20 anos.'.format(mulheres))
