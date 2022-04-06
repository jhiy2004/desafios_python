LIMITE = 80


def multar(velocidade):
    custo = (velocidade - LIMITE)*7
    return round(custo, 2)


velocidade = float(input('Qual é a velocidade atual do carro? '))
if(velocidade > LIMITE):
    custo = multar(velocidade)
    print(
        f'\033[31mMULTADO! Você excedeu o limite permitido que é de {LIMITE}Km/h')
    print(
        f'\033[31mVocê deve pagar uma multa de \033[m\033[93mR${custo}!\033[m')
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
