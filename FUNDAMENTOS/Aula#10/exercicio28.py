#Crie um programa que pense em um numero inteiro entre 1 a 5 e peça para o usurio tentar descobrir.
#E o programa deverá escrever na tela se ele acertou ou não

import random
import time

print('Vamos brincar de advinhação, advinhe qual numero estou pensando')
n1 = random.choice([1,2,3,4,5])

n2 = int(input('Digite um numero de 1 a 5: '))
print('PROCESSANDO...')
time.sleep(2)
if n2 == n1:
    print('Parabens, você acertou o numero {}'.format(n1))
else:
    print('Que pena, eu estava pensando em {}'.format(n1))