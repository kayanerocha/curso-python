##########################################################################################
#                 Função que mostra o manual dos comandos que o usuário solicitar        #
##########################################################################################

from time import sleep


def mostraTitulo(titulo, cor):
    """
    -> Mostra os títulos do programa.
    :param titulo: título que deseja imprimir.
    :param cor: cor de fundo para o título.
    :return: sem retorno.
    """
    print(f'\033[{cor}m')
    print(f'~' * (len(titulo) + 4))
    print(f'  {titulo}  ')
    print('~' * (len(titulo) + 4))
    print('\033[m')
    sleep(0.5)

def interactiveHelp(comando):
    """
    -> Mostra o manual de um comando.
    :param comando: comando que o usuário deseja ver o manual.
    :return: sem retorno.
    """
    mostraTitulo(f"Acessando o manual do comando '{comando}'", 46)
    
    print('\033[0;30;47m')
    help(comando)
    print('\033[m')
    sleep(0.5)
    
while True:
    mostraTitulo('SISTEMA DE AJUDA PyHELP', 42)
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() in 'FIM':
        break
    interactiveHelp(comando)

mostraTitulo('ATÉ LOGO!', 41)