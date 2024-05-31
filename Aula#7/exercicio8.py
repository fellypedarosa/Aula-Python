#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

n1 = int(input('Digite quantos metros: '))

centimetros = n1 * 100
milimetros = centimetros * 10

print('Em {} metros tem {} contimetros \nE {} metros tem {} milimetros.'.format(n1,centimetros,n1,milimetros))