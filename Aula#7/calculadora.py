n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))


so = (n1 + n2)
su = (n1 - n2)
div = (n1 / n2)
mult = (n1 * n2)
pot = (n1 ** n2)

calculo = input('Digite SO para soma, SU para subtração, DIV para divisão, MULT para multiplicação e POT para potencia:').lower()

if calculo == 'pot':
    if n2 == 2:
        print('O resultado da potencia de {} ao quadrado é: {}'.format(n1,pot))      
    else:
        print('O resultado da potencia de {} ao cubo é: {}'.format(n1,pot))

if calculo == 'so':
    print('O resultado da soma de {} com {} é {}'.format(n1,n2,so))
elif calculo == 'su':    
    print('O resultado da subtração de {} com {} é {}'.format(n1,n2,su))
elif calculo == 'div':    
    print('O resultado da divisão de {} com {} é {:.3f}'.format(n1,n2,div))
elif calculo == 'mult':    
    print('O resultado da multiplicação de {} com {} é {}'.format(n1,n2,mult))
else:
    print()
                     
