c = float(input('Digite a temperatura em graus: '))
print('A temperatura de {}{}ºC{} corresponde a {}{}ºF!{}'.format('\033[33m', c, '\033[m', '\033[35m', c * 1.8 + 32,
                                                                 '\033[m'))
