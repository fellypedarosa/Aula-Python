n1 = int(input('Digite seu \033[34mnumero: \033[m'))
n2 = int(input('Digite seu \033[34mnumero: \033[m'))
# sem especificar o tipo da variavel(str, int, float ou bool) ele iria apenas concatenar o valor de n1 com n2(n1=10 e n2=20:  1020)
so = (n1 + n2)
su = (n1 - n2)

resultado = input('Digite se quer soma ou subtração com \033[33mSU \033[mou \033[33mSO: \033[m').lower()
 #lower converte qualquer entrada do usuario para minuscula
 
if resultado == 'so':
     print('O resultado da soma entre {} e {} é: {}'.format(n1,n2,so))   
elif resultado == 'su':
     print('O resultado da subração entre {} e {} é : {}'.format(n1,n2,su))     
else:
     print('Algo de errado não está certo')