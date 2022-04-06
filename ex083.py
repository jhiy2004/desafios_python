expressao = input('Digite a expressão: ')
parenteses = []
for c in expressao:
    if c == '(' or c == ')':
        parenteses.append(c)
        
if len(parenteses) % 2 == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
