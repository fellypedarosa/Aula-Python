#Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR

print('Vamos verificar se seu numero é PAR ou IMPAR')

n1 = int(input('Digite um numero: '))
par = n1 % 2

if par == 0:
    print('Seu numero é PAR!')
else:
    print('Seu numero é IMPAR!')