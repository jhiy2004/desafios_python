import contas

preco = float(input('Digite o preço: R$'))

print(f'A metade de R${preco} é R${contas.metade(preco)}')
print(f'O dobro de R${preco} é R${contas.dobro(preco)}')
print(f'Aumentando 10%, temos R${contas.dez_porcento(preco)}')