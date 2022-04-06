def dissecador(variavel):
    print(f'O tipo primitivo desse valor é {type(variavel)}')
    print(f'Só tem espaços?  {variavel.isspace()}')
    print(f'É um número? , {variavel.isnumeric()}')
    print(f'É alfabético? , {variavel.isalpha()}')
    print(f'É alfanumérico? {variavel.isalnum()}')
    print(f'Está em maiúsculo? {variavel.isupper()}')
    print(f'Está em minúsculo? {variavel.islower()}')
    print(f'Está captalizado? {variavel.istitle()}')


v = input('Digite algo: ')
dissecador(v)
