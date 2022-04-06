print('Gerador de PA')
print('-='*10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
acrescenta = 1
limite = 10
contador = 1
termo = 0

print(primeiro_termo, end=' → ')
while acrescenta != 0:
    while contador < limite:
        termo = primeiro_termo + razao*contador
        contador += 1
        print(termo, end=' → ')
    print('PAUSA')
    acrescenta = int(input('Quantos termos você quer mostrar a mais? '))
    limite += acrescenta
print(f'Progressão finalizada com {contador} termos mostrados.')
