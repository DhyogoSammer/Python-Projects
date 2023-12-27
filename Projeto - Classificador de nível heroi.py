# # 1️⃣ Desafio Classificador de nível de Herói

#**O Que deve ser utilizado**

#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões

## Objetivo

#Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 5.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói de nome **{nome}** está no nível de **{nivel}**"


while True :
    heroi = str(input('Digite o nome do Heroi : '))
    nivel = int(input('Digite a quantidade de Xp do Heroi : '))
    if nivel < 1000 :
        print(f'O Heroi de nome {heroi} está no nível de Ferro ')
    elif nivel >= 1001 and nivel <= 2000:
        print(f'O Heroi de nome {heroi} está no nível de Bronze ')
    elif nivel >= 2001 and nivel <= 5000 :
        print(f'O Heroi de nome {heroi} está no nível de Prata ')
    elif nivel >= 5001 and nivel <= 7000 :
        print(f'O Heroi de nome {heroi} está no nível de Ouro ')
    elif nivel >= 7001 and nivel <= 8000 :
        print(f'O Heroi de nome {heroi} está no nível de Platina ')
    elif nivel >= 8001 and nivel <= 9000 :
        print(f'O Heroi de nome {heroi} está no nível de Ascedente ')
    elif nivel >= 9001 and nivel <= 10000 :
        print(f'O Heroi de nome {heroi} está no nível de Imortal ')
    else :
        print(f'O Heroi de nome {heroi} está no nível de Radiante ')
    perg = str(input('Deseja sair ? [S/N]')).upper().strip()[0]
    if perg == 'S':
        break 
print('OBRIGADO PELA PARTICIPAÇÃO :) !')
    


 