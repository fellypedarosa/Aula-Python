#Faça um programa que leia um numero inteiro e mostre sem sucessor e antecessor

cor = {'verde': '\033[1;32m','azul': '\033[1;34m', 'limpa':'\033[m'}
n1 = int(input('Digite um numero inteiro para saber seu {}antecessor{} e{} sucessor: {}'.format(cor['verde'],cor['limpa'],cor['azul'],cor['limpa'])))

antecessor = n1 - 1
sucessor = n1 + 1

print('O antecessor de {}{}{} é {}{}{} \nE o sucessor de {}{}{} é {}{}{}.'.format(cor['verde'],n1,cor['limpa'],cor['azul'],antecessor,cor['limpa'],cor['verde'],n1,cor['limpa'],cor['azul'],sucessor,cor['limpa'],))

#n1, antecessor,   n1,sucessor