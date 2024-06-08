#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiusculas,
# o nome com todas as letras minusculas, quantas letras ao todo sem considerar espaços e quantas letras tem o primeiro nome.

frase = input('Qual seu nome? ').strip()

print('Maiusculo: ',frase.upper())
print('Minusculo: ', frase.lower())

frase2 = frase.split()

#frase3 = ''.join(frase2)
print('Seu nome tem ',len(frase) - frase.count(' '), ' letras sem contar os espaços')
print('Seu nome tem ',len(frase), ' letras com os espaços')
print('Seu primeiro nome é: ',frase2[0])



