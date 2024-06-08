#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 5% de aumento.
sl = float(input('Desculpe a pergunta, mas qual é o seu salario: '))

aumento = (sl * 5) / 100
salario = sl + aumento

print('Parabens! seu novo salario com 5 % de aumento será de: {}R$'.format(salario))