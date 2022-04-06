from random import randint

tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: ', end='')
print(*tupla, end=' ')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
    