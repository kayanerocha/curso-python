from ex115 import mensagens
from time import sleep

def pessoas_cadastradas():
    mensagens.titulo('PESSOAS CADASTRADAS')

    try:
        with open('./mundo3/exercicios/ex115/pessoas_cadastradas.txt', 'r', encoding='utf8') as arquivo:
            for l in arquivo:
                pessoa = l.split(',')
                idade = pessoa[1].replace('\n', '')
                print(f'{pessoa[0]:<30} {idade}')
    except Exception as erro:
        print(f'{mensagens.cores[1]}Ocorreu um erro na leitura do arquivo: {erro.__class__}{mensagens.cores[0]}')
    finally:
        sleep(0.5)
        mensagens.menu()

def cadastrar_pessoa():
    mensagens.titulo('NOVO CADASTRO')

    while True:
        try:
            nome = str(input('Nome: '))
        except:
            print(f'{mensagens.cores[1]}Entrada inválida.{mensagens.cores[0]}')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print(f'{mensagens.cores[1]}ERRO: por favor, digite um número inteiro válido.{mensagens.cores[0]}')
        except Exception as erro:
            print(f'{mensagens.cores[1]}Entrada inválida. {erro.__class__}{mensagens.cores[0]}')
        else:
            break
    
    try:
        with open('./mundo3/exercicios/ex115/pessoas_cadastradas.txt', 'a', encoding='utf8') as arquivo:
            arquivo.write(f'{nome}, {idade} anos\n')
    except:
        print(f'{mensagens.cores[1]}Erro no cadastro de pessoa.{mensagens.cores[0]}')
    else:
        print(f'Novo registro de {nome} adicionado.')
        sleep(0.5)
    
    mensagens.menu()