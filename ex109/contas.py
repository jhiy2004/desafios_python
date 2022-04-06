def metade(preco, formatado=True):
    res = preco/2
    return res if not formatado else formatar(res)

def dez_porcento(preco, formatado=True):
    res = preco*1.1
    return res if not formatado else formatar(res)

def dobro(preco, formatado=True):
    res = preco*2
    return res if not formatado else formatar(res)

def formatar(preco=0,moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')