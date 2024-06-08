#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados: 
# EX: 1834 
# unidade: 4 
# dezena: 3 
# centena: 8 
# milhar: 1 

n1 = int(input('Digite um numero de 0 a 9999: '))

'''print('unidade: ',n1[3])
print('dezena: ',n1[2])
print('centena: ',n1[1])
print('milhar: ',n1[0])'''

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('unidade: ', u)
print('dezena: ', d)
print('centena: ', c)
print('milhar: ', m)
