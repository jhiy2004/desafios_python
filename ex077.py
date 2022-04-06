palavras = ('APRENDER', 'PROGRAMAR','LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
        
for p in palavras:
    print(f'Na palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
    print()