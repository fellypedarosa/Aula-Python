#Desenvolva um programa que pergunte a distancia de uma viagem em km e calcule o preço da passagem,
# cobrando R$0,50 por km para viajens de até 200km e R$0,45 para viajens mais longas

print('Vamos calcular o preço da sua passagem!')

pas = int(input('Qual a distancia você vai percorrer em Km: '))

if pas <= 200:
    print('A passagem será de {}R$'.format(pas * 0.50))
else:
    print('Como você irá percorrer mais de 200Km, o valor da passagem será de {}R$'.format(pas * 0.45))

print('Tenha uma boa viajem!')

