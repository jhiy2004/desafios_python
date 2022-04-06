from random import randint
from time import sleep

def sortear_lista():
    qtd = 5
    lista = []
    print(f'Sorteando {qtd} valores da lista: ', end='')
    for _ in range(qtd):
        num = randint(1,10)
        print(num, end=' ', flush=True)
        sleep(.4)
        lista.append(num)
    print('PRONTO!')
    return lista

def somar_pares(lista):
    pares = [p for p in lista if p % 2 == 0]
    return sum(pares)

lista_sorteada = sortear_lista()
print(f'Somando os valores pares de {lista_sorteada}, temos {somar_pares(lista_sorteada)}')