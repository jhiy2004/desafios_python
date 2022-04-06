def pode_formar_triangulo(r1, r2, r3):
    if (r1 + r2) == r3:
        return False
    elif (r1+r2) > r3:
        return True


def tipo_triangulo(r1, r2, r3):
    if r1 == r2 == r3:
        return 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r3 == r2:
        return 'ISÓSCELES'
    else:
        return 'ESCALENO'


print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
tipo = tipo_triangulo(reta1, reta2, reta3)

if pode_formar_triangulo(reta1, reta2, reta3):
    print(f'{reta1} x {reta2} x {reta3} PODEM formar um triângulo, {tipo}')
else:
    print(f'{reta1} x {reta2} x {reta3} NÃO PODEM formar um triângulo')
