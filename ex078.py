lista = [int(input(f'Digite um valor para a Posição {x}: ')) for x in range(5)]
posicao_maior = [posicao for posicao,valor in enumerate(lista) if valor == max(lista)]
posicao_menor = [posicao for posicao,valor in enumerate(lista) if valor == min(lista)]

print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')