print('='*30)
print('BANCO CEV'.center(30))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
resto = valor
cedulas = [50, 20, 10, 1]

for c in cedulas:
    print(f'Total de {resto // c} cédulas de R${c}') if resto // c > 0 else False
    resto %= c
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')