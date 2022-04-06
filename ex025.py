def verifica_string(nome):
    for n in nome.split(' '):
        if(n.upper() == 'SILVA'):
            return True
    return False


nome = input('Digite o seu nome completo: ').strip()

print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}")
