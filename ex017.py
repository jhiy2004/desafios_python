from math import hypot


def calc_hipotenusa(a, b):
    c = (a**2 + b**2)**0.5
    return round(c, 2)


a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
c = calc_hipotenusa(a, b)
hipotenusa = hypot(a, b)

print(
    f'A hipotenusa em um triângulo de cateto oposto {a} e cateto adjacente {b} é {c}')
