# Projeto Sistema Bancário

deposito = 0
saldo = 0
saque = ''
extrato_bancário = 0
msg = 'Seja Bem Vindo ao Banco Nordeste!'
tam = len(msg)

print('~' * tam)
print(msg.upper())
print('~' * tam)
perg = 0
d = 0
saq = 0 
while perg != 5 :
    perg = int(input('O que você deseja fazer ? [1] - Deposito, [2] - Saque ou [3] - Extrato, [4] - Ver Saldo ou [5] - Sair : \n'))
    if perg == 5 :
        print('SAINDO...\n')

    #DEPOSITO

    elif perg == 1 :
        print('DEPOSITO SELECIONADO\n')
        while True : 
            deposito = float(input('Quanto você deseja depositar ? \n'))
            if deposito > 0 :
                print(f'Depositando {deposito}R$ na sua conta\n')
                d += 1 
                extrato_bancário += deposito 
                print(f'{deposito}R$ DEPOSITADO COM SUCESSO\n')
                perg = int(input('Deseja sair ? [1] - Sim ou [2] - Não : \n'))
                if perg == 1 :
                    break
                elif perg == 2 :
                    deposito = float(input('Quanto você deseja depositar ? \n'))
                    if deposito > 0 : 
                        print(f'Depositando mais {deposito}R$\n')
                        d += 1 
                        extrato_bancário += deposito 
                        print(f'{deposito}R$ DEPOSITADO COM SUCESSO\n')
                        perg = int(input('Deseja sair ? [1] - Sim ou [2] - Não : \n'))
                        if perg == 1 :
                            break
                    else :
                        print('VALORES NEGATIVOS NÃO PODEM SER DEPOSITADOS\n')
                        deposito = float(input('Digite o valor novamente :\n'))
                        while deposito < 0 :
                            deposito = float(input('Digite o valor novamente :\n'))
                            if deposito > 0 :
                                print(f'Depositando {deposito}R$ na sua conta\n')
                                d += 1 
                                extrato_bancário += deposito 
                                print(f'{deposito}R$ DEPOSITADO COM SUCESSO\n')
                        perg = int(input('Deseja sair ? [1] - Sim ou [2] - Não : \n'))
                        if perg == 1 :
                            break 

            elif deposito < 0 :
                while deposito < 0 : 
                    print('VALORES NEGATIVOS NÃO PODEM SER DEPOSITADOS\n')
                    deposito = float(input('Digite o valor novamente :\n'))
                if deposito > 0 :
                    print(f'Depositando {deposito}R$ na sua conta\n')
                    extrato_bancário += deposito 
                    print(f'{deposito}R$ DEPOSITADO COM SUCESSO\n')
                perg = int(input('Deseja sair ? [1] - Sim ou [2] - Não : \n'))
                if perg == 1 :
                    break 


    #SAQUE
    elif perg == 2 :
        print('SAQUE SELECIONADO\n')
        saldo = extrato_bancário
        if saldo != 0 :
            cont = 3 
            while cont != 0 :
                saque = float(input('Quando deseja sacar ? \n'))
                print(f'Saldo disponivel {saldo}R$\n')
                if saldo < 0 :
                    print('NÃO PODEMOS REALIZAR A OPERAÇÃO POIS VOCÊ NÃO TEM DINHEIRO SUFICIENTE PARA SACAR ESSE VALOR\n')
                    break 
                else :
                    if saque <= 500 : 
                        saldo -= saque 
                        cont -= 1 
                        print(f'SACANDO {saque} R$\n')
                        saq += 1 
                        print(f'SOBROU {saldo} R$ da sua conta\n')
                        extrato_bancário -= saque 
                        perg = int(input(f'Deseja sair ? [1] - Sim ou [2] - Não , Quantidade de saques disponiveis {cont} : \n'))
                        if perg == 1 :
                            break 
                        if cont == 0 :                     
                            print('LIMITE DE 3 SAQUES POR DIA ATINGIDO\n')
                            print('FINALIZANDO O PROCESSO DE SAQUE\n')
                    else :
                        print('SÓ PODE SACAR VALORES MENORES QUE 500 REAIS\n')

        else :
            print(f'Seu saldo atual é de {saldo} R$ deposite algo para sacar\n')

    #EXTRATO
    elif perg == 3 :
        if extrato_bancário == 0 :
            print(f'EXTRATO ATUAL {extrato_bancário} R$\n')
            print('NÃO FORAM REALIZADO MOVIMENTAÇÕES NA CONTA\n')
        else : 
            print('EXTRATO SELECIONADO\n')
            print(f'VOCÊ POSSUI {extrato_bancário} R$\n')
            print(f'Ao total foram realizados {d} depositos e {saq} saques\n')
    #SALDO
        
    elif perg == 4 :
        print('SALDO SELECIONADO\n')
        saldo = extrato_bancário
        print(f'SALDO ATUAL {saldo} R$\n')
    else :
        print('ERROR NA DIGITAÇÃO DO NÚMERO\n')
        