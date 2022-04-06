import contas

def formatar(preco=0,moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

preco = float(input('Digite o preço: R$'))

print(f'A metade de {formatar(preco)} é {formatar(contas.metade(preco))}')
print(f'O dobro de {formatar(preco)} é {formatar(contas.dobro(preco))}')
print(f'Aumentando 10%, temos {formatar(contas.dez_porcento(preco))}')