preco_normal = float(input('Preço normal R$'))
print('''Escolha uma condição de pagamento:
1 - À vista dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
condicao_pagamento = int(input('Opção: '))
novo_preco = 0
if condicao_pagamento == 1:
    novo_preco = preco_normal - (preco_normal * 0.1)
elif condicao_pagamento == 2:
    novo_preco = preco_normal - (preco_normal * 0.05)
elif condicao_pagamento == 3:
    novo_preco = preco_normal
    parcela = novo_preco / 2
    print('Sua compra será parcela em 2x de R${:.2f}.'.format(parcela))
elif condicao_pagamento == 4:
    num_parcelas = int(input('Quantas parcelas? '))
    novo_preco = preco_normal + (preco_normal * 0.2)
    parcela = novo_preco / num_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(num_parcelas, parcela))
else:
    total = preco_normal
    print('Opção inválida.')

print('Sua compra de R${} vai custar R${} no final'.format(preco_normal, novo_preco))