extensos = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numeros = {0: 'zero',1: 'um',2: 'dois',3:'três',4: 'quatro',5:'cinco',6:'seis',7:'sete',8:'oito',9:'nove',10:'dez',11:'onze',12:'doze',13:'treze',14:'catorze',15:'quinze',16:'dezesseis',17:'dezessete',18:'dezoito',19:'dezenove',20:'vinte'}

numero = int(input('Digite um número entre 0 e 20: '))
while numero < 0 or numero > 20:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))

for n, e in numeros.items():
    if n == numero:
        print(f'Você digitou o número {e}')
print(f'Você digitou o número {extensos[numero]}')