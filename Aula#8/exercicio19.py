#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo  no nome do escohido 

import random

print('Digite os nomes de 5 alunos: ')

lista = input('Digite os nomes separando por virgula: ')

nome = lista.split(',')

##########################PODE SER ASSIM TMB##################################
# n1 = input('Primeiro nome: ')
# n2 = input('Segundo nome: ')
# n3 = input('Terceiro nome: ')
# n4 = input('Quarto nome: ')
#alunos = [n1,n2,n3,n4]
#sorteia = random.choice(alunos)
##########################PODE SER ASSIM TMB##################################
sorteia = random.choice(nome)

print('O aluno sorteado foi: {}'.format(sorteia))



