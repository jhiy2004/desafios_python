def verifica_opcao(valor, opc):
    if opc == 1:
        total = round(valor*0.90, 2)
    elif opc == 2:
        total = round(valor*0.95, 2)
    elif opc == 3:
        total = round(valor, 2)
        parcelado = total / 2
        print(f'Sua compra será parcelada em 2x de R${parcelado}')
    elif opc == 4:
        parcelas = int(input('Quantas parcelas? '))
        total = round(valor*1.2, 2)
        print(
            f'Sua compra será parcelada em {parcelas}x de R${total/parcelas} COM JUROS')
    else:
        total = 0
        print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    print(f'Sua compra de R${valor} vai custar R${total} no final')


print(f"{'='*10}LOJA YAMAOKI{'='*10}")
preco = float(input('Digite o valor gasto na loja: R$'))
opcao = int(input("""
[1] À visto dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão

Digite sua opção: """))
verifica_opcao(preco, opcao)
