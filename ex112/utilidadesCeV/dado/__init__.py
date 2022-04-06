def leia_dinheiro(txt):
    while True:
        dinheiro = input(txt).strip().replace(',','.')
        if dinheiro.isalpha() or dinheiro == '':
            print(f'\033[31mERRO: "{dinheiro}" é um preço inválido!\033[m')
        else:
            break
    return float(dinheiro)