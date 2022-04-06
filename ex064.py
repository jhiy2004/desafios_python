num = 0
lista = []
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    lista.append(num)
print(f'Você digitou {len(lista)} números e a soma entre eles é {sum(lista)}')
