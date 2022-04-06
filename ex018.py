import math

angulo = float(input('Digite o valor de um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno de {angulo}° = {round(seno, 2)}')
print(f'O cosseno de {angulo}° = {round(cosseno,2)}')
print(f'A tangente de {angulo}° = {round(tangente, 2)}')
