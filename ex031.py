def calc_valor_viagem(km):
    if km > 200:
        return round(0.45 * km, 2)
    return round(0.5 * km, 2)


distancia = float(input('Digite a distância de sua viagem: '))
passagem = calc_valor_viagem(distancia)
print(f'Uma viagem de {distancia}Km custará R${passagem}')
