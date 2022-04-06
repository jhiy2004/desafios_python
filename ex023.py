numero = input('Digite um número: ')

while len(numero) < 4:
    numero = '0'+numero

inteiro = int(numero)
u = inteiro // 1 % 10
d = inteiro // 10 % 10
c = inteiro // 100 % 10
m = inteiro // 1000 % 10

print(f'Unidade: {numero[-1]} ___ {u}')
print(f'Dezena: {numero[-2]} ___ {d}')
print(f'Centena: {numero[-3]} ___ {c}')
print(f'Milhar: {numero[-4]} ___ {m}')
