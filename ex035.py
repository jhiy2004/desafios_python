def pode_formar_triangulo(r1, r2, r3):
    if (r1 + r2) == r3:
        return False
    elif (r1+r2) > r3:
        return True


print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if pode_formar_triangulo(reta1, reta2, reta3):
    print(f'{reta1} x {reta2} x {reta3} PODEM formar um triângulo')
else:
    print(f'{reta1} x {reta2} x {reta3} NÃO PODEM formar um triângulo')
