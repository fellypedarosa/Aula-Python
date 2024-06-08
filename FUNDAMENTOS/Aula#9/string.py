#Fatiamento de String
'''exemplo = [E|S|T|U|D|A|N|D|O| |F|A|T|I|A|M|E|N|T|O| |D|E| |S|T|R|I|N|G]
              0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9

                            De 0 até 29 micro espaços
                                
exemplo[4] --> D

exemplo[10:21] --> FATIAMENTO (Não marca o 21, vai até o espaço anterior: 20)

exemplo[10:31] --> FATIAMENTO DE STRING (como não existe micro espaço 30 e 31 ele vai sómente até 29)

exemplo[10:20:2] --> FTAET (ele foi de 10 a 20 porém pulando 2)

exemplo[:9] --> ESTUDANDO

exemplo[24:] --> STRING

exemplo[10::3] --> FIEOETN -->  (Foi do 10 até o final pulando 3 espaços)

len(exemplo) --> 29 (len pergunta quantos micro espaços tem a nossa string, que contando com o 0 tem 29 espaços)

exemplo.count('E') --> 3 (count conta quantas vezes a letra aparece na nossa string)

exemplo.count('E',0,10) --> 1 ( de 0 até 10 só tem uma letra E)

exemplo.find('ING') --> 27 (está dizendo que a combinação ing começa na posição 27)

exemplo.rfind('N') --> 28 (A primeira vez que N aparece contando da direita para esquerda é na 28 posição)

exemplo.find('PALAVRÃO') --> -1 ( como ele não achou nenhuma combinação palavrão, ele retorna -1)

'FATIAMENTO' in exemplo --> True (na pergunta "existe a combinação FATIAMENTO em exemplo" ele retorna True pois existe, ou False se não existisse)

exemplo.replace('ESTUDANDO', 'APRENDENDO') --> A|P|R|E|N|D|E|N|D|O| |F|A|T|I|A|M|E|N|T|O| |D|E| |S|T|R|I|N|G (ele substituiu estudando por aprendendo)

exemplo.upper() (se houvesse alhuma letra em minusculo ele jogaria para maiusculo)

exemplo.lower() --> estudando fatiamento de string (joga para minusculo)

exemplo.capitalize() --> Estudando fatiamento de string (Ele escreve toda a frase para minusculo, porém a primeira letra da primeira palavra seria maiuscula)

exemple.title() --> Estudando Fatiamento de String (Ele reescreve toda a frase como minusculo porém a primeira letra de cada palavra fica maiuscula)
######################################################################################################
exemplo2 = [| | | |E|S|T|U|D|A|N|D|O| |F|A|T|I|A|M|E|N|T|O| |D|E| |S|T|R|I|N|G| | |]

exemplo2.strip() --> [E|S|T|U|D|A|N|D|O| |F|A|T|I|A|M|E|N|T|O| |D|E| |S|T|R|I|N|G] (Remove espaços desnecessarios)

exemplo2.rstrip() --> | | | |E|S|T|U|D|A|N|D|O| |F|A|T|I|A|M|E|N|T|O| |D|E| |S|T|R|I|N|G| (Remove somente os epaços da direita)

exemplo2.lstrip() --> |E|S|T|U|D|A|N|D|O| |F|A|T|I|A|M|E|N|T|O| |D|E| |S|T|R|I|N|G| | | (Remove somente os espaços da esquerda)
######################################################################################################

exemplo3.split() --> [E|S|T|U|D|A|N|D|O|], [|F|A|T|I|A|M|E|N|T|O|], [|D|E|], [|S|T|R|I|N|G] (onde tiver espaço ele ira dividir como uma nova frase(refazendo os indices ou os numeros de cada micro espaço de acordo com cada palavra, recomeçando a cada palavra. 0 1 2 3 4 5 6...))
                     0 1 2 3 4 5 6 7 8      0 1 2 3 4 5 6 7 8 9      0 1      0 1 2 3 4 5
                     
'-'.join(exemplo3) --> |E|S|T|U|D|A|N|D|O|-|F|A|T|I|A|M|E|N|T|O|-|D|E|-|S|T|R|I|N|G| 
                        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 (0 - 29)'''
         
frase = 'Fellype o Mais Brabo'
#print(frase[7::2])

#print('''Eles querem que você se sinta mal
#Pois assim eles se sentem bem
#Eu nasci pobre
#Mas não nasci otário
#Eu é que não caio
#No conto do vigário
#Eu tenho fé em Deus
#Pra resolver qualquer parada
#Chega com respeito
#Na minha quebrada
#Eu não vim pra me explicar
#Eu vim pra confundir
#Eu não vim pra me explicar''')

#print(frase.replace('Mais','Maior'))

frase = frase.replace('Mais','Maior') #Salva a troca de mais por maior do replace na variavel frase
#print(frase)

#print(frase.lower().find('maior'))

dividido = frase.split()

#print(dividido[2]) #mostrar só o segundo item da lista

print(dividido[2] [3]) #Dentro do segundo item da minha lista, mostre a letra no terceiro espaço