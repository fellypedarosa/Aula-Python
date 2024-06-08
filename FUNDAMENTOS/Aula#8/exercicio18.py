#Um prograam que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math

a = int(input('Qual o valor do angulo: '))

#Aqui o sin, cos e tan vai entender o x como radiando e não como graus. Então precisamos converter usando math.radians
seno = math.sin(math.radians(a))
coss = math.cos(math.radians(a))
tang = math.tan(math.radians(a))

print('O valor do seno é: {:.3f} \nO valor do Cosseno é: {:.3f} \nE o valor da tangente é: {:.3f}'.format(seno,coss,tang))

