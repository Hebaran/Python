from random import randint
from os import system

permissionList = [0, 1]
higherProbabilityList = []
higherProbability = count = totalWins = totalDefeats = errors = 0

exitVerify_YesNot = ["SIM", "S", "YES", "Y" "NÃO", "NAO", "N", "Ñ", "NO", "NOT"]
exitVerifyYes = ["SIM", "S", "YES", "Y"]
exitVerifyNot = ["NÃO", "NAO", "N", "Ñ", "NO", "NOT"]

userMoney = userMoneyInitial = 1000.00

system('cls')


while True: # PROGRAMA
    while True:
        if errors == 0:
            print(f"Seu saldo atual é: R$ {userMoney:.2f}\n")
        
        userNumber = int(input("Escolha um número [0/1]: "))
        
        if userNumber not in permissionList:
            print("\n[ERRO 001] Opção inválida.")
            errors += 1
        
        else:
            break
        
    while True:       
        if count == 0:
            count += 1    
            higherProbability = (userMoney * 0.001) # 0.1%
            
            print(f"\nO valor que o usuário deve apostar para aumentar suas chances de ganhar deve ser: R$ {higherProbability:.2f}")
    
        else:
            if higherProbability == 0:
                higherProbability = (userMoney * 0.001) # 0.1%
                    
                print(f"\nO valor que o usuário deve apostar para aumentar suas chances de ganhar deve ser: R$ {higherProbability:.2f}")
            
            else:
                if userMoney != 0:
                    print(f"\nO valor que o usuário deve apostar para aumentar suas chances de ganhar deve ser: R$ {higherProbability:.2f}")
                                
        while True:
            recommendedBet = str(input("Deseja apostar o valor recomendado? [S/N] ")).strip().upper()
        
            if recommendedBet not in exitVerify_YesNot:
                print("\n[ERRO 005] Opção inválida.")
            
            else:
                break
                
        if recommendedBet in exitVerifyYes:
            if higherProbability > userMoney:
                print("\n[ERRO 004] Opção inválida, seu valor atual é menor do que o valor recomendado.\n")
                
                while True:
                    allInConfirmation = str(input(f"Deseja dar All In R$ ({userMoney:.2f})? [S/N] ")).strip().upper()
                    
                    if allInConfirmation not in exitVerify_YesNot:
                        print("[ERRO 007] Opção inválida.")
                    
                    else:
                        if allInConfirmation in exitVerifyYes:
                            bet = userMoney
                            
                        else:
                            while True:
                                bet = float(input("\nQual valor deseja apostar? R$ "))
    
                                if bet > userMoney:
                                    print("\n[ERRO 002] Saldo insuficiente, tente novamente.")
                
                                elif bet <= 0:
                                    print("\n[ERRO 003] É impossível apostar esse valor.")
                
                                else:
                                    higherProbabilityList.append(bet)
                    
                                    break
                        
                        break
            else:    
                bet = higherProbability
                higherProbabilityList.append(bet)
        
        else:
            while True:
                bet = float(input("\nQual valor deseja apostar? R$ "))
    
                if bet > userMoney:
                    print("\n[ERRO 002] Saldo insuficiente, tente novamente.")
                
                elif bet <= 0:
                    print("\n[ERRO 003] É impossível apostar esse valor.")
                
                else:
                    higherProbabilityList.append(bet)
                    
                    break
        
        break

    while True: # ESCOLHA DO VENCEDOR
        num = randint(0, 1)
        
        print(f"\nO número sorteado foi: {num}")
        print(f"O número escolhido pelo usuário foi: {userNumber}")
        
        if userNumber == num: # GANHOU
            userMoney += bet
            totalWins += 1
            errors = 0
            
            higherProbabilityList.clear()
            higherProbability = 0
            
            print(f"\nParabéns, você ganhou!")
            print(f"O valor recebido foi de: R$ {bet:.2f}")
            print(f"\nSeu saldo atual é de: R$ {userMoney:.2f}")
            
            break
        
        else: # PERDEU
            userMoney -= bet
            higherProbability = 0
            totalDefeats += 1
            errors = 0
            
            print(f"\nQuer azar, não foi dessa vez.")
            print(f"O valor perdido foi de: R$ {bet:.2f}")
            print(f"\nSeu saldo atual é de: R$ {userMoney:.2f}")
            
            for c in higherProbabilityList:
                higherProbability += c
            
            higherProbability += higherProbabilityList[0]
            
            break
    
    print()
    
    if userMoney <= 0: # FECHAR O PROGRAMA CASA O USUÁRIO ZERAR O SALDO
        print("Estamos encerrando o programa...\n")
        
        break
    
    while True:
        exitScript = str(input("Deseja continuar? [S/N] ")).strip().upper()
        
        if exitScript not in exitVerify_YesNot:
            print("\n[ERRO 004] Opção inválida, verifique sua resposta e tente novamente.")
        
        else:
            print("Estamos encerrando o programa...\n")
            
            break
    
    if exitScript in exitVerifyYes:
        system('cls')
    
    else:
        print()
        
        break

userProfits = userMoney - userMoneyInitial
totalGames = totalWins + totalDefeats

system('cls')

print(f"SEU SALDO INICIAL FOI: R$ {userMoneyInitial:.2f}")
print(f"SEU SALDO FINAL FOI:   R$ {userMoney:.2f}")
print(f"SEU LUCRO TOTAL FOI:   R$ {userProfits:.2f}\n")
print(f"QUANTIDADE DE JOGOS QUE VOCÊ TEVE FOI:    {totalGames}")
print(f"QUANTIDADE DE VITÓRIAS QUE VOCÊ TEVE FOI: {totalWins}")
print(f"QUANTIDADE DE DERROTAS QUE VOCÊ TEVE FOI: {totalDefeats}\n")
