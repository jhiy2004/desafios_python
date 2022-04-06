produtos = ('Lápis',1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
for p in produtos:
    if isinstance(p, str):
        print(f'{p:.<30}',end='')
    else:
        print(f'R${p:>7.2f}') 
print('-'*40)