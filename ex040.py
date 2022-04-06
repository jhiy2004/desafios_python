nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
if media < 5.0:
    print('\033[31mREPROVADO\033[m')
elif media >= 5.0 and media <= 6.9:
    print('\033[34mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')
