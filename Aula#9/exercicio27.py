#Um programa que leia o nome completo de uma pessoa, e mostre o primeiro e o último nome separadamente 
# EX Ana Maria de Souza 
# Primeiro: Ana 
# Ultimo: Souza

nome = input('Digite seu nome: ').strip()
nome = nome.title()
nome = nome.split()

print('Primeiro: ',nome[0])
print('Ultimo: ',nome[len(nome)-1])