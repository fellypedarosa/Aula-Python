#O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos, 
# faça um programa que leia os nomes dos queatro alunos e mostre a ordem sorteada

#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo  no nome do escohido 

import random

print('Digite os nomes de 4 alunos: ')

lista = input('Digite os nomes separando por virgula: ')

nome = lista.split(',')

random.shuffle(nome)

print('A ordem dos alunos sorteados foi:', ', '.join(nome))



