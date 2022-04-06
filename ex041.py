from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Idade é {idade}, MIRIM')
elif idade <= 14:
    print(f'Idade é {idade}, INFANTIL')
elif idade <= 19:
    print(f'Idade é {idade}, JÚNIOR')
elif idade <= 25:
    print(f'Idade é {idade}, SÊNIOR')
else:
    print(f'Idade é {idade}, MASTER')
