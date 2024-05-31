#Um programa que leia as duas notas de um aluno e calcule e mostre a media do aluno 
n1 = float(input('Digite uma das notas do aluno: '))
n2 = float(input('Digite a outra nota do aluno: ' ))

media = (n1 + n2) /2

print('A media entre {} e {} é igual a: {}.'.format(n1,n2,media))