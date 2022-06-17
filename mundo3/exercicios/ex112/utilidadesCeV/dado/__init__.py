##########################################################################################
#                                   Valida a entrada do valor                            #
##########################################################################################

def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).strip()
        is_monetario = True
        if not valor.isnumeric():
            for c in valor:
                if c.isalpha():
                    is_monetario = False
                    break
        if is_monetario and valor != '':
            break
        print(f'\033[0;31mERRO: "{valor}" é um preço inválido!\033[m')
    
    if ',' in valor:
        valor = valor.replace(',', '.')
    return float(valor)