#Faça um programa que leia um numero inteiro e mostre sem sucessor e antecessor

n1 = int(input('Digite um numero inteiro para saber seu antecessor e sucessor: '))

antecessor = n1 - 1
sucessor = n1 + 1

print('O antecessor de {} é {} \nE o sucessor de {} é {}.'.format(n1,antecessor,n1,sucessor))