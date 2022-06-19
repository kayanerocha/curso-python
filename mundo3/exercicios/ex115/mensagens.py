from ex115 import pessoas
from time import sleep


cores = ['\033[m', # 0 - nada
    '\033[0;31m', # 1 - vermelho
    '\033[0;33m', # 2 - amarelo
    '\033[0;34m', # 3 - azul

    ]

def linha():
    print('-' * 40)

def titulo(titulo):
    tamanho = len(titulo)
    linha()
    print(titulo.center(40))
    linha()

def menu():    
    while True:
        titulo('MENU PRINCIPAL')
        print(f'''{cores[2]}1{cores[0]} - {cores[3]} Ver pessoas cadastradas {cores[0]}
{cores[2]}2{cores[0]} - {cores[3]} Cadastrar nova pessoa {cores[0]}
{cores[2]}3{cores[0]} - {cores[3]} Sair do Sistema {cores[0]}''')
        linha()

        try:
            opcao = int(input(f'{cores[2]}Sua opção: {cores[0]}'))
        except:
            print(f'{cores[1]}ERRO! Digite uma opção válida!{cores[0]}')
            sleep(1)
        else:
            match opcao:
                case 1:
                    pessoas.pessoas_cadastradas()
                    break
                case 2:
                    pessoas.cadastrar_pessoa()
                    break
                case 3:
                    titulo('Saindo do sistema... Até logo!')
                    exit()
                case _:
                    print(f'{cores[1]}ERRO! Digite uma opção válida!{cores[0]}')
                    sleep(0.5)