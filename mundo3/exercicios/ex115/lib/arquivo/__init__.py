from ex115.lib import interface
from time import sleep

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt') # modo de leitura de arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+') # modo de escrita de texto e se não existir cria o arquivo
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')

def pessoas_cadastradas():
    interface.titulo('PESSOAS CADASTRADAS')

    try:
        with open('./mundo3/exercicios/ex115/pessoas_cadastradas.txt', 'r', encoding='utf8') as arquivo:
            for l in arquivo:
                pessoa = l.split(',')
                idade = pessoa[1].replace('\n', '')
                print(f'{pessoa[0]:<30} {idade}')
    except Exception as erro:
        print(f'{interface.cores[1]}Ocorreu um erro na leitura do arquivo: {erro.__class__}{interface.cores[0]}')
    finally:
        sleep(0.5)
        interface.menu()

def cadastrar_pessoa():
    interface.titulo('NOVO CADASTRO')

    while True:
        try:
            nome = str(input('Nome: '))
        except:
            print(f'{interface.cores[1]}Entrada inválida.{interface.cores[0]}')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print(f'{interface.cores[1]}ERRO: por favor, digite um número inteiro válido.{interface.cores[0]}')
        except Exception as erro:
            print(f'{interface.cores[1]}Entrada inválida. {erro.__class__}{interface.cores[0]}')
        else:
            break
    
    try:
        with open('./mundo3/exercicios/ex115/pessoas_cadastradas.txt', 'a', encoding='utf8') as arquivo:
            arquivo.write(f'{nome}, {idade} anos\n')
    except:
        print(f'{interface.cores[1]}Erro no cadastro de pessoa.{interface.cores[0]}')
    else:
        print(f'Novo registro de {nome} adicionado.')
        sleep(0.5)
    
    interface.menu()