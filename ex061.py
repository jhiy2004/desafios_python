primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
proximo_termo = primeiro_termo
limite = primeiro_termo + razao * 9

print(primeiro_termo, end=' → ')
while proximo_termo < limite:
    proximo_termo += razao
    print(proximo_termo, end=' → ')
print('FIM')