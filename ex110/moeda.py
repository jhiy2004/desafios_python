def cabecalho(titulo, tam):
    print('-'*tam)
    print(titulo.center(tam))
    print('-'*tam)

def aumentar(preco,taxa=0, formatado=True):
    res = preco + (preco*taxa)/100
    return res if not formatado else formatar(res)

def diminuir(preco,taxa=0, formatado=True):
    res = preco - (preco*taxa)/100
    return res if not formatado else formatar(res)

def metade(preco, formatado=True):
    res = preco/2
    return res if not formatado else formatar(res)

def dobro(preco, formatado=True):
    res = preco*2
    return res if not formatado else formatar(res)

def formatar(preco=0,moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco, aumento=10, reducao=5):
    cabecalho('RESUMO DO VALOR', 40)
    print(f'Preço analisado: \t{formatar(preco)}')
    print(f'Dobro do preço: \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento)}')
    print(f'{reducao}% de redução: \t{diminuir(preco,reducao)}')
    print('-'*40)

if __name__ == '__main__':
    print('Hello from my module!')