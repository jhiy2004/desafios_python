print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
qtd_termos = int(input('Quantos termos você quer mostrar? '))
lista = []
print('~'*20)
for n in range(qtd_termos):
    if n == 0:
        termo = 0
    elif n == 1:
        termo = 1
    else:
        termo = (lista[-1]) + (lista[-2])
    lista.append(termo)
    print(termo, end=' → ')
print('FIM')
print('~'*20)