##########################################################################################
#        Função que recebe 3 parâmetros: início, fim e passo e realiza 3 contagens       #
##########################################################################################
from time import sleep

def imprimeLinha():
    print('-=' * 30)

def solicitaValores():
    print('Agora é sua vez de personalizar a contagem!')
    
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    return [inicio, fim, passo]

def contador(inicio, fim, passo):
    imprimeLinha()

    passo = 1 if passo == 0 else abs(passo)

    print(f'Contagem de {inicio } até {fim} de {passo} em {passo}')
    sleep(2.5)

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end= ' ', flush=True) # não liga o buffer de tela nesse print, para o sleep funcionar
            sleep(0.5)
    else:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ', flush=True) # não liga o buffer de tela nesse print
            sleep(0.5)

    print('FIM!')

def executaContagem():
    contador(1, 10, 1)
    contador(10, 0, 2)

    v = solicitaValores()
    contador(v[0], v[1], v[2])

executaContagem()

    