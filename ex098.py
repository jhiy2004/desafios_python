from time import sleep

def contagem_personalizada(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo = -1
        print(f'Passo igual zero não é permitido, valor alterado para {passo}')
    for n in range(inicio, fim+1 if passo > 0 else fim-1, passo):
        print(n, end=' ', flush=True)
        sleep(.4)
    print('FIM!')

print('-='*30)
contagem_personalizada(1, 10, 1)

print('-='*30)
contagem_personalizada(10, 0, -2)

print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

print('-='*30)
contagem_personalizada(inicio, fim, passo)
