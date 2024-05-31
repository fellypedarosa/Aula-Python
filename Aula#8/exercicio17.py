#Um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triangulo e retangulo e mostre 
# o comprimento da hipotenusa

#     CATEYO OPOSTO -->    |\ 
#     CATEYO OPOSTO -->    | \     <--- HIPOTENUSA
#     CATEYO OPOSTO -->    |  \
#     CATEYO OPOSTO -->    |___\
#                          
#                            ^
#                            |
#                   CATETO ADJACENTE  
#
from math import hypot

co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))

teorema_pitagoras = hypot(co,ca)

print('A soma dos quadrados dos catetos é igual o valor da hipotenusa: {:.2f}'.format(teorema_pitagoras))