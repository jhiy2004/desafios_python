def aumento_salarial(salario):
    if salario > 1250.00:
        return round(salario * 1.1, 2)
    else:
        return round(salario * 1.15, 2)


salario = float(input('Digite o salário do funcionário: R$'))
salario_aumentado = aumento_salarial(salario)

print(
    f'O salário do funcionário que era R${salario}, passou a ser de R${salario_aumentado}')
