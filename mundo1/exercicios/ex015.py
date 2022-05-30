formata = {'limpa': '\033[m',
           'negri-azul': '\033[1:34m',
           'vermelho': '\033[31m'}

dias = int(input('{}Digite a quantidade de dias alugado: '.format(formata['negri-azul'])))
km = float(input('Digite a quantidade de quilômetros rodados:{} '.format(formata['limpa'])))
pago = (dias * 60) + (km * 0.15)
print('{}O total a pagar é de R${:.2f}{}'.format(formata['vermelho'], pago, formata['limpa']))
