##########################################################################################
#                   Função que recebe o ano de nascimento e diz uma pessoa               #
#                           tem voto negado, opcional ou obrigatório                     #
##########################################################################################
from datetime import datetime

def voto(ano_nascimento):
    """
    -> Verifica se o voto do usuário é negado, opcional ou obrigatório.
    :param ano_nascimento: ano de nascimemto do usuário.
    :return: valor literal.
    Função criada por Kayane Rocha.
    """
    idade = datetime.now().year - ano_nascimento
    voto = ''
    if idade < 16:
        voto = 'NEGADO'
    elif idade < 18:
        voto = 'OPCIONAL'
    else:
        voto = 'OBRIGATÓRIO'
    
    return f'Com {idade} anos: VOTO {voto}.'

print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))