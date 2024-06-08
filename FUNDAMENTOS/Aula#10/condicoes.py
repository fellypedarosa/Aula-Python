import emoji
###Condição simples###
'''nome = str(input('Qual seu nome meu nobre?'))
nome = nome.title()

if nome == 'Fellype':
    print('Nome tri!')
    
print('Vamos continuar {}'.format(nome))'''

###Condição composta###

nome = str(input('Qual seu nome meu consagrado?'))
nome = nome.title()

if nome == 'Fellype':
    print(emoji.emojize('Agora tu veio :sunglasses:', language='alias'))
else:
    print('Que nome bobo')
    
print('Enfim, vamos continuar {}'.format(nome))

print('Cara seu nome é tão maneiro' if nome == 'Fellype' else 'Pena que vc não se chama Fellype hehe')