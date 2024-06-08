#Crie um programa que leia o nome da sua cidade e diga se a cidade começa com 'santo'

nome = input('Qual o nome da sua cidade: ').strip()
nome = nome.title()

santo = 'Santo' in nome[0:5]

if santo == True:
    print('Que legal, sua cidade tem santo no nome')
else:
    print('Que bela cidade!')