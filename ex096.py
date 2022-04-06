def calc_area_terreno(largura, comprimento):
    area = largura * comprimento
    return area

print(' Controle de Terrenos')
print('-'*15)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area = calc_area_terreno(largura, comprimento)
print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')