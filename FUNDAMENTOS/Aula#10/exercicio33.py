#Faça um programa que leia três numeros e mostre qual o maior e qual é o menor 

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))

print('###### MAIOR NUMERO ######')
if n1 >= n2 and n1 >= n3:
    print('{} é o maior numero!'.format(n1))
if n2 >= n1 and n1 >= n3:
    print('{} é o maior número!'.format(n2))
if n3 >= n1 and n3 >= n2:
    print('{} é o maior número!'.format(n3))
    
print('##### MENOR NUMERO #####')

if n1 <= n2 and n1 <= n3:
    print('{} é o menor numero!'.format(n1))
if n2 <= n1 and n2 <= n3:
    print('{} é o menor número!'.format(n2))
if n3 <= n1 and n3 <= n2:
    print('{} é o menor número!'.format(n3))
