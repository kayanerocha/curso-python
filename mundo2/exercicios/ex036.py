valor_casa = float(input('Valor da casa R$'))
salario = float(input('Salário R$'))
anos_pagar = float(input('Em quantos anos vai pagar? '))

mensalidade = valor_casa / (anos_pagar * 12)
limite = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(valor_casa, anos_pagar, mensalidade))
if mensalidade <= limite:
    print('Empréstimo aprovado.')
else:
    print('Empréstimo negado.')