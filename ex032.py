from datetime import date


def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False


ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
isbissexto = bissexto(ano)

if isbissexto:
    print(f'O ano {ano} É BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
