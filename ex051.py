# termo = int(input('Digite o primeiro termo: '))
# razao = int(input('Digite a razão: '))

# print(termo, end=' -> ')
# res = termo
# for i in range(9):
#     res = res+razao
#     print(res, end=' -> ')

# print('ACABOU')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + 9 * razão
for c in range(primeiro, décimo + razão, razão):
    print(c, end=' → ')
print('ACABOU')