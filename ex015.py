def calcula_aluguel_carro(dias, km):
    valor_aluguel = (60*dias) + (0.15*km)
    return round(valor_aluguel, 2)


dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de Km rodados: '))
valor_aluguel = calcula_aluguel_carro(dias, km)

print(f'O total a pagar é de R${valor_aluguel}')
