#crie um programa que leia um nome e diga se ele tem silva, em qualquer lugar do nome
nome = input('Digite seu nome: ').strip()
nome = nome.title()

silva = 'Silva' in nome

if silva == True:
    print('Dá um chute numa moita cai um silva haha')
else:
    print('Belo nome!')