def print_especial(msg):
    tam_msg = len(msg) + 4
    print('~'*tam_msg)
    print(msg.center(tam_msg))
    print('~'*tam_msg)

print_especial('Gustavo Guanabara')
print_especial('Curso de Python no Youtube')
print_especial('CeV')