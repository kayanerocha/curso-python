from ex115.lib.interface import menu
from ex115.lib.arquivo import *

caminho_arquivo = './mundo3/exercicios/ex115/pessoas_cadastradas.txt'
if not arquivo_existe(caminho_arquivo):
    criar_arquivo(caminho_arquivo)
    
menu()
