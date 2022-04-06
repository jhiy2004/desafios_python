def area_parede(largura, altura):
    area = largura*altura
    return area


def calcula_tinta(area):
    qtd_tinta = area/2
    return qtd_tinta


largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = area_parede(largura, altura)
qtd_tinta = calcula_tinta(area)
print(
    f'Sua parede tem a dimensão de {largura} x {altura}m e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {qtd_tinta}l de tinta')
