def linha(tam=20):
    return '+'+'-'*tam+'+'


def menu(lst):
    i = 1
    print(linha())
    for opc in lst:
        print('|'+f'[{i}] {opc}'.center(20)+'|')
        i += 1
    print(linha())


inteiro = int(input('Digite um número inteiro: '))
menu(['BIN', 'OCT', 'HEX'])
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'{inteiro} convertido para BINÁRIO é igual a {bin(inteiro)[2:]}')
elif opcao == 2:
    print(f'{inteiro} covertido para OCTAL é igual a{oct(inteiro)[3:]}')
elif opcao == 3:
    print(f'{inteiro} covertido para HEXADECIMAL é igual a {hex(inteiro)[2:]}')
else:
    print('\033[31mDigite um opção válida.\033[m')
