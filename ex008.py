def conversor_medidas(metros):
    todas_medidas = {'mm': 10**-3, 'cm': 10**-2,
                     'dm': 10**-1, 'dam': 10**1, 'hm': 10**2, 'km': 10**3}
    for k, v in todas_medidas.items():
        todas_medidas.update({k: v*metros})
    return todas_medidas


metros = float(input('Digite um valor em metros: '))
todas_medidas = conversor_medidas(metros)
print(todas_medidas)
for medida, valor in todas_medidas.items():
    print(f'{metros} metros em \033[32m{medida}\033[m = {valor} {medida}')
