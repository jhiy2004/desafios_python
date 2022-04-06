valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos_financiamento = int(input('Quantos anos de financiamento? '))
prestacao_mensal = valor_casa/(anos_financiamento*12)

print(
    f'Para pagar uma casa de R${round(valor_casa,2)} em {anos_financiamento} anos a prestação será de R${round(prestacao_mensal, 2)}')
if prestacao_mensal < salario*0.3:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
