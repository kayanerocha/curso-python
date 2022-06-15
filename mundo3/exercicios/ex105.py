##########################################################################################
#   Função que recebe várias notas de alunos e retorna um dicionário com as informações  #
##########################################################################################

def notas(*notas, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    media = sum(notas) / len(notas)
    informacoes = {'total': len(notas),
                'maior': max(notas),
                'menor': min(notas),
                'media': media}
    if situacao:
        if media < 5:
            informacoes['situacao'] = 'RUIM'
        elif media < 7:
            informacoes['situacao'] = 'RAZOÁVEL'
        else:
            informacoes['situacao'] = 'BOA'
    
    return informacoes

resp = notas(6, 6, 6, 6.5, situacao=True)
print(resp)