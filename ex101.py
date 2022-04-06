def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade >= 18 and idade <= 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 16 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')

print('-'*30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)