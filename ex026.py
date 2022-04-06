frase = input('Digite uma frase: ').strip().upper()

while True:
    letra = input(
        'Digite um letra que deseje procurar na frase: ').strip().upper()
    if len(letra) > 1:
        print('\033[31mPor favor digite apenas um caractere.\033[m')
    else:
        break


print(f"A letra '{letra}' aparece {frase.count(letra)} vezes na sua frase")
print(
    f"A letra '{letra}' aparece pela primeira vez na posição {frase.find(letra)+1}")
print(
    f"A letra '{letra}' aparece pela última vez na posição {frase.rfind(letra)+1}")
