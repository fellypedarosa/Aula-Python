#crie um programa que leia um numero e real e informe apenas sua parte inteira: 6.150 = Parte inteira igual a: 6


from math import trunc
#import math --> se eu fizesse isso, precisaria especificar an variavel com: math.floor

n1 = float(input('Digute um numero com virgua sem virgula kk: '))

calcula = trunc(n1)
#calcula = math.floor(n1) --> Ai ficaria assim

print('O numero inteiro de {} é: {}'.format(n1,calcula))