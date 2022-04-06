def real_para_dolar(real):
    cotacao_dolar = 3.27
    dolar = real / cotacao_dolar
    return round(dolar, 2)


real = float(input('Digite quanto dinheiro você tem em real: R$ '))
print(f'Você pode comprar US$ {real_para_dolar(real)}')
