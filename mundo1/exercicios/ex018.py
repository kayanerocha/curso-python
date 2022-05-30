import math

angulo = int(input('\033[7mDigite o ângulo:\033[m '))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('\033[31mO seno de {}º é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}\033[m'.format(angulo, seno, cosseno,
                                                                                               tangente))
