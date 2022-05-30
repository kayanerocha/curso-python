reta1 = int(input('\033[36mReta 1: '))
reta2 = int(input('Reta 2: '))
reta3 = int(input('Reta 3:\033[m '))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('\033[32mAs retas formam um triângulo.\033[m')
else:
    print('\033[31mAs retas não formam um triângulo\033[m')