def desconta_preco(preco):
    novo_preco = preco - (preco * 5/100)
    return round(novo_preco, 2)


preco = float(input('Digite o preço do produto: R$'))
novo_preco = desconta_preco(preco)
print(
    f'O produto que custava R${preco}, com o desconto de 5% passou a custar R${novo_preco}')
