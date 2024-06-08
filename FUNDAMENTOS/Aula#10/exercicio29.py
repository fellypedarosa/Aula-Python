#Escreva um pograma que leia a velocidade de um carro e se ele ultrapassar 80km por hora, mostre uma mensagem 
# dizendo que foi multado, a multa vai custar 7 reais por cada km acima do limite 
print('Parado, aqui é a brigada, o limite de velocidade aqui é 80Kmh!')

n1 = int(input('Qual velocidade voce estava andando: '))
n2 = n1 - 80
n3 = n2 * 7

if n1 <= 80:
    print('Muito bem, continue andando sob o limite de velocidade!')
else:
    print('Voce estava andando a {}, e isso é {}Kmh acima do limite. \nMagrão vou te multar em {}R$ pois são 7,00R$ por kilometro acima do limite!'.format(n1,n2,n3))
    
    
    