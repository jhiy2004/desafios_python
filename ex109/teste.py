import contas

preco = float(input('Digite o preço: R$'))

print(f'A metade de {contas.formatar(preco)} é {contas.metade(preco)}')
print(f'O dobro de {contas.formatar(preco)} é {contas.dobro(preco)}')
print(f'Aumentando 10%, temos {contas.dez_porcento(preco)}')