num = 0
lista = []
while num != 999:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    lista.append(num)
print(f'Foram digitados {len(lista)} números, e a soma entre eles é {sum(lista)}')