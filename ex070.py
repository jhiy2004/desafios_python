produtos = []

print('-'*30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'*30)

while True:
    nome_produto = input('Nome do produto: ')
    preco_produto = float(input('Preço: R$'))
    produto = (nome_produto, preco_produto)
    produtos.append(produto)
    opc = ' '
    while opc not in 'SN':
        opc = input('Quer continuar? [S/N] ').upper()
    if opc == 'N':
        break
    print('-'*30)

preco_barato = mais_de_mil = total = 0
nome_barato = ''
for p in produtos:
    if total == 0:
        preco_barato = p[1]
        nome_barato = p[0]
    total += p[1]
    if p[1] > 1000:
        mais_de_mil += 1
    if p[1] < preco_barato:
        preco_barato = p[1]
        nome_barato = p[0]
print(produtos)
print('-'*10,'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi R${total}')
print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${preco_barato}')
