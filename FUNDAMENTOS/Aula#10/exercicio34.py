#Crie um programa que leia o comprimento de de tres retas e diga se elas podem formar um triangulo

print('Vamos verificar o tamanhos das retas')

r1 = int(input('Digite o tamanho de uma reta: '))
r2 = int(input('Digite o tamanho de outra reta: '))
r3 = int(input('Digite o tamanho de mais uma reta: '))

if r1 + r2 < r3:
    print('Não é um triangulo!')
elif r1 + r3 < r2:
    print('Não é um triangulo!')
elif r2 + r3 < r1:
    print('Não é um triangulo!')
else:
    print('É um triangulo!')