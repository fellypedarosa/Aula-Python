#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento 
#Para salarios superior a 1.250,00 calcule um aumento de 10%
#Para salarios inferiores ou iguais a 1.250,00 o aumento é de 15%

salario = int(input('Qual o seu salario: '))

if salario >= 1250:
    print('Seu aumento será 10% que dará {}R$'.format(((salario * 10) / 100) + salario))
else:
    print('Seu aumento será de 15% que dará {}R$'.format(((salario * 15) / 100) + salario))