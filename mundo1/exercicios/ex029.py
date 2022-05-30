velocidade = float(input("\033[1;34mVelocidade em Km/h:\033[m "))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('\033[31mVocê foi multado. A multa é de R${:.2f}\033[m'.format(multa))