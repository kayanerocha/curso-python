n = int(input('Número da tabuada desejada: '))
for i in range(0, 11):
    r = n * i
    print('{} * {} = {}'.format(n, i, r))