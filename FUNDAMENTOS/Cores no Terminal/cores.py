# ################################ PADRÃO ANSI ##############################################
#                                                                                                                       
#         \033     [    0     ;          33       ;      44 m     
#               !_____________!___________________!___________________________                                                       
#               | style       |  text             |     background(fundo)                                                        
#               !_____________!___________________!___________________________                                                                         
#               | 0 nada      |  30: branco       |     40: branco                                                  
#               | 1 negrito   |  31: vermelho     |     41: vermelho            ###################################                                     
#               | 4 sublinhado|  32: verde        |     42: verde               #                                 #
#               | 7 negativo  |  33: amarelo      |     43: amarelo             # \033[m <===Volta tudo ao padrão #                                  
#               |             |  34: azul         |     44: azul                #                                 #
#               |             |  35: lilas        |     45: lilas               ###################################                                                     
#               |             |  36: verde agua   |     46: verde agua                                                                              
#               |             |  37: cinza        |     47: cinza                                                                              
## ################################ PADRÃO ANSI ##############################################                                                                                                 
                                                                                                                 
print('\033[0;33;44m Olá mundo!\033[m')
print('\033[1;36;45m Olá mundo!\033[m')
print('\033[7;30;0m Olá mundo!\033[m')
print('\033[4;30;45m Olá mundo!\033[m')

v = 'VERMELHA'
l = 'LILAS'
a = 'AMARELA'
print('ESSA É A COR \033[31m{}\033[m, ESSA É A COR \033[35m{}\033[m E ESSA É A COR \033[33m{}\033[m'.format(v,l,a))
print('ÉSSA É UMA FORMA MUITO MAIS BONITA DE DEIXAR FORMATADDO A COR {}{}{}, POR EXEMPLO!!!'.format('\033[31m', v ,'\033[m'))

cores = {'limpa':'\033[m',     #POR ENQUANTO ESSA FUNÇÃO É NOVO, E NÃO FOI BEM EXPLICADA                                                                              
         'azul':'\033[34m',   #POR ENQUANTO ESSA FUNÇÃO É NOVO, E NÃO FOI BEM EXPLICADA                                                                              
         'verde':'\033[32m',   #POR ENQUANTO ESSA FUNÇÃO É NOVO, E NÃO FOI BEM EXPLICADA  
         'amarelo':'\033[33m'}   #POR ENQUANTO ESSA FUNÇÃO É NOVO, E NÃO FOI BEM EXPLICADA  

print('COM ESSA {}FORMA EU SIMPLESMENTE {}POSSO COLOCAR DENTRO DAS {}MINHAS CHAVES{} A VARIAVEL DENTRO {}DA MINHA TABELA{} DE CORES...'.format(cores['amarelo'],cores['limpa'],cores['verde'],cores['limpa'],cores['azul'],cores['limpa']))                                                                            
         
                                                 