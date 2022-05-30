# Curso em Video Python

# Fatiamento
    # frase[9] imprime o caractere da posicao 9
    # frase[9:13] imprime os caracteres da posicao 9 ate a 12
    # frase[9:21:2] imprime os caracteres entre a 9 e 21 pulando duas posicoes
    # frase[:5] = frase[0:5]
    # frase[15:] imprime a partir do caractere 15 ate o final da string
    # frase[9::3] comeca no 9 pulando 3 posicoes

# Analise
    # len(frase) comprimento da frase
    # frase.count('o') conta quantas vezes aparece a letra o
    # frase.count('o', 0, 13) quantas vezes aparece a letra o entre 0 e 13, o 13 nao conta
    # frase.find('deo') mostra em que posicao comecou deo
    # frase.find('Android') se colocar uma frase que nao existe retorna -1
    # 'Curso' in frase diz se a palavra curso existe na frase

# Transformacao
    # frase.replace('Python', 'Android') troca python por android
    # frase.upper() deixa em maiusculo
    # frase.lower() deixa em minusculo
    # frase.capitalize() deixa somente a primeira letra da frase em maiuscula
    # frase.title() deixa a primeira letra de cada palavra em maiuscula
    # frase.strip() remove os espacos inuteis no inicio e final da string
    # frase.rstrip() remove somente os espacos da direita inuteis
    # frase.lstrip() remove somente os espacos da esquerda inuteis

# Divisao
    # frase.split() divide a string considerando os espacos e refaz os indices de cada palavra

# Juncao
    # '-'.join(frase) junta todos os elementos da frase e usa o separador - nos espacos antigos

frase = 'Curso em Video Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('curso'))
print(frase.lower().find('video'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])  # letra 3 da palavra 2

print("""Midnight
You come and pick me up, no headlights
A long drive
Could end in burning flames or paradise
Fade into view - oh!
It's been a while since I have even heard from you
Heard from you""")