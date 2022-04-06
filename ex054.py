from datetime import date

ano_atual = date.today().year
maioridade = 0
menoridade = 0

for n in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {n}° pessoa nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maioridade+=1
    else:
        menoridade+=1

print(f'Ao todo tivemos {maioridade} pessoas maiores de idade.')
print(f'Ao todo tivemos {menoridade} pessoas menores de idade.')
