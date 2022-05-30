nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:<20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:^20}'.format(nome))
print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('A soma é {}, a subtração é {}, \n o produto é {}, '.format(s, su, m), end=' >>> ')
print('a divisão é {}, a inteira é {}, o resto é {} e a exponeciação é {}'.format(d, di, r, e))
