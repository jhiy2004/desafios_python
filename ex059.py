from time import sleep

def linha(tam=15):
    return '=-'*15

def menu(opcs):
    i = 1
    for opc in opcs:
        print(f'[ {i} ] {opc}')
        i += 1

def somar(v1,v2):
    res = v1+v2
    print(f'A soma entre {v1} + {v2} é {res}')

def multiplicar(v1,v2):
    res = v1*v2
    print(f'O resultado de {v1} x {v2} é {res}')

def maior(v1,v2):
    if v1 > v2:
        print(f'{v1} é maior que {v2}')
    elif v2 > v1:
        print(f'{v2} é maior que {v1}')
    else:
        print(f'Os dois valores são iguais')

def entrada_valores():
    valor1 = float(input('Primeiro valor: '))
    valor2 = float(input('Segundo valor: '))
    return valor1, valor2

opcoes = ['somar', 'multiplicar', 'maior', 'novos números', 'sair do programa']
opcao = 0
valor1, valor2 = entrada_valores()

while opcao != 5:
    menu(opcoes)
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        somar(valor1,valor2)
    elif opcao == 2:
        multiplicar(valor1,valor2)
    elif opcao == 3:
        maior(valor1,valor2)
    elif opcao == 4:
        valor1, valor2 = entrada_valores()
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
    print(linha())
sleep(1)
print('Fim do programa! Volte sempre!')