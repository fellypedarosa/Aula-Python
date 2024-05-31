#Faça um programa que leia a altura e largura de uma parede em metros e calcule sua area e a quantidade de tinta 
# necessária para pinta-la. Sabendo que cada litro de tinta pinta uma area de 2m²

a1 = float(input('Qual a altura da parede em metros: '))
l1 = float(input('Qual a largura da parede em metros: '))

area = a1 * l1
litros = area / 2

print('Sabemos que a area total da parede é: {:.0f}m² \nEntão será necessario {} litros de tinta'.format(area,litros))
