while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for n in range(1,11):
        res = num * n
        print(f'{num} x {n} = {res}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')