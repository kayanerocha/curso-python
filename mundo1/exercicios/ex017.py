import math

co = float(input('\033[35mCateto oposto: '))
ca = float(input('Cateto adjacente:\033[m '))
h = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
print('\033[36mA hipotenusa vale {:.2f}\033[m'.format(h))
