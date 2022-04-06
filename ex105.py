def notas(*notas, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma
    """
    media = sum(notas) / len(notas)
    dicionario = {'total': len(notas), 'maior': max(notas), 'menor': min(notas), 'média': media}
    if sit:
        if media < 5:
            dicionario['situação'] = 'RUIM'
        elif media < 8:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'ÓTIMO'     
    return dicionario

resp = notas(1,5.5,10,9.7, sit=True)
print(resp)