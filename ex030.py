def par_ou_impar(n):
    if n % 2 == 0:
        print(f'O número {n} é \033[34mPAR\033[m')
    else:
        print(f'O número {n} é \033[34mÍMPAR\033[m')


numero = int(input('\033[35mDigite um número:\033[m '))
par_ou_impar(numero)
