def aumento_salarial(salario):
    novo_salario = salario + (salario * 15/100)
    return round(novo_salario, 2)


salario = float(input('Digite o salário do funcionário: R$'))
novo_salario = aumento_salarial(salario)
print(
    f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R$4967.34')
