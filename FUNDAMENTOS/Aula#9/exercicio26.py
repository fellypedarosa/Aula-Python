#Crie um programa que leia uma frase e diga: Quantas vezes aparece a letra A,
# em qual posição ela aparece pela primeira vez e qual posição ela aparece por ultimo
frase = input('Digite uma frase: ').strip()
frase = frase.lower()

print('Sabia que a letra A aparece ',frase.count('a'), ' vezes na sua frase?')

print('E sabia que a letra A parece pela primeira vez na posição ',frase.find('a'))

print('E sabia também que a letra A parece pela ultima vez na posição ',frase.rfind('a'))