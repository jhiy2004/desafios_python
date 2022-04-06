def precoVista(preco):
    preco_vista = preco - (preco*10/100)
    return round(preco_vista, 2)


def precoParcelado(preco):
    preco_parcelado = preco + (preco*8/100)
    return round(preco_parcelado, 2)


preco = float(input('Digite o preco do produto: R$'))
preco_vista = precoVista(preco)
preco_parcelado = precoParcelado(preco)

print(
    f'O preço normal do produto é {preco}, parcelado fica a R${preco_parcelado}, mas caso deseja pagar à vista terá um desconto de 10%, que ficaria R${preco_vista}')
