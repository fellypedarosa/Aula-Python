#Crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz qudrada.

n1 = int(input('DIgite um numero para saber o dobro, triplo e raiz quadrada: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
#É assim que é a raiz quadrada

print('O dobro de {} é: {} \nO triplo de {} é: {} \nE a raiz quadrada de {} é igual a: {}'.format(n1,dobro,n1,triplo,n1,raiz))