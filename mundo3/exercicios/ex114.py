##########################################################################################
#        Funções que leiam números inteiros e reais usando tratamento de exceções        #
##########################################################################################

from urllib.request import urlopen

try:
    urlopen('http://pudim.com.br/')
except:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[0;33mConsegui acessar o site Pudim com sucesso!\033[m')