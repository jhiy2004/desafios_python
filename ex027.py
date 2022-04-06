nome_completo = input('Digite o seu nome completo: ').strip()
primeiro_nome = nome_completo.split(' ')[0]
ultimo_nome = nome_completo.split(' ')[-1]

print(f'Muito prazer em te conhecer {nome_completo}!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')
