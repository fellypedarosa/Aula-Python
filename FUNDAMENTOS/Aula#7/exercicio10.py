#Um programa que leia quantos reais uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
n1 = float(input('Quantos reais você tem? '))

conversor = n1 / 5.16

print('Com {}R$ você teria {:.2f}$ dolares.'.format(n1,conversor))