salario = float(input('\033[33mSalário R$\033[m'))
if salario > 1250:
    novo_salario = salario + (salario * 0.1)
else:
    novo_salario = salario + (salario * 0.15)
print('\033[34mQuem ganhava R${:.2f} passa a ganhar R${:.2f} agora.\033[m'.format(salario, novo_salario))