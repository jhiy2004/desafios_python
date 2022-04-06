def status_imc(imc):
    if imc < 18.5:
        return 'Abaixo do Peso'
    elif imc <= 25:
        return 'Peso ideal'
    elif imc <= 30:
        return 'Sobrepeso'
    elif imc <= 40:
        return 'Obesidade'
    else:
        return 'Obesidade Mórbida'


peso = float(input('Digite o seu peso em quilos: '))
altura = float(input('Digite a sua altura em metros: '))
imc = round(peso/altura**2, 1)
status = status_imc(imc)

print(f'O IMC dessa pessoa é de {imc}')
print(f'Você está na faixa de {status}')
