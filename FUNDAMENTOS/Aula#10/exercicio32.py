#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
print('Vamos saber se um ano é Bissexto ou não')

'''ano = int(input('Digite um ano: '))
bissexto = ano % 4
secular = ano % 100
secular1 = (ano % 100) % 400

if ano == secular:
    secular2 = ano % 400
    if secular2 == 0:
        print('Essa foi de fude')

if bissexto == 0:
    print('O ano {} é Bissexto!'.format(ano))
elif secular1 == 0:
    print('Esse ano não só é bissexto quanto é multiplo de 100 e divisivel por 400')
else:
    print('Esse ano não é bissexto')'''
    
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
