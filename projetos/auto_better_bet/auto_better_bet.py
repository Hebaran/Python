from random import randint
from time import sleep
from os import system


def zero_number_left(value):
    value_format = len('{0:.2f}'.format(value))
    value_format = int(value_format) + 1

    if -10 < value < 10:
        return '{0:0{1}.2f}'.format(value, value_format).replace(".", ",")

    else:
        return '{0:.2f}'.format(value).replace(".", ",")


system('cls')

global bet, userProfits, totalGames

userNumber = randint(0, 1)
permissionList = [0, 1]
higherProbabilityList = []
higherProbability = totalWins = totalDefeats = totalLossesInaRow = count = 0

while True:
    try:
        userMoney = userMoneyInitial = maximumMoneyReached = float(input("Com quanto dinheiro deseja entrar no Auto_Better_Bet? R$ "))
        
        if userMoney <= 0:
            system('cls')
            print(f"[ERRO 001] É impossível apostar: R$ {zero_number_left(userMoney)}")
        
        else:
            break
    
    except ValueError:
        system('cls')
        print("[ERRO 002] É impossível apostar este valor")
    
    except KeyboardInterrupt:
        system('cls')
        print("Malandrinho você ein, hahaha.")

system('cls')

try:
    while True: # PROGRAMA
        if True:
            print(f"Seu saldo atual é:      \033[32mR$ {zero_number_left(userMoney)}\033[m\n")

        while True:
            if count == 0:
                count += 1
                higherProbability = (userMoneyInitial * 0.0005)

                print(f"\nO valor que o usuário deve apostar para aumentar suas chances de ganhar deve ser: \033[33mR$ {zero_number_left(higherProbability)}\033[m")

            else:
                if higherProbability == 0:
                    higherProbability = (userMoneyInitial * 0.0005)

                    print(f"\nO valor que o usuário deve apostar para aumentar suas chances de ganhar deve ser: \033[33mR$ {zero_number_left(higherProbability)}\033[m")

                else:
                    if userMoney != 0:
                        print(f"\nO valor que o usuário deve apostar para aumentar suas chances de ganhar deve ser: \033[33mR$ {zero_number_left(higherProbability)}\033[m")

            if higherProbability > userMoney:
                print("\n[ERRO 004] Opção inválida, seu valor atual é menor do que o valor recomendado.\n")

                if True:
                    bet = userMoney

            else:
                bet = higherProbability
                higherProbabilityList.append(bet)

            break

        while True: # ESCOLHA DO NÚMERO VENCEDOR
            num = randint(0, 1)

            print(f"\n- Jogo número: {(totalWins + totalDefeats) + 1}")
            print(f"O número sorteado foi:  {num}")
            print(f"O número escolhido foi: {userNumber}")

            if userNumber == num: # GANHOU
                userMoney += bet
                totalWins += 1
                totalLossesInaRow = 0

                higherProbabilityList.clear()
                higherProbability = 0

                if userMoney >= maximumMoneyReached:
                    maximumMoneyReached = userMoney

                print(f"\nParabéns, você ganhou!")
                print(f"O valor ganho foi de:   \033[32mR$ {zero_number_left(bet)}\033[m")

                if userNumber == 0:
                    userNumber = 1

                else:
                    userNumber = 0

                break

            else: # PERDEU
                userMoney -= bet
                higherProbability = 0
                totalDefeats += 1
                totalLossesInaRow += 1

                print(f"\nQuer azar, não foi dessa vez.")
                print(f"O valor perdido foi de: \033[31mR$ {zero_number_left(bet)}\033[m")

                if totalLossesInaRow % 8 == 0 and totalLossesInaRow != 0:
                    higherProbability = (userMoneyInitial * 0.0005)

                else:
                    for c in higherProbabilityList:
                        higherProbability += c

                    higherProbability += higherProbabilityList[0]

                break
        
        print('\n\n\033[34mPRESSIONE A QUALQUER MOMENTO PARA ENCERRAR O PROGRAMA: \033[31mCTRL + C\033[m\n')
        sleep(0.1)

        if userMoney <= 0: # FECHA O PROGRAMA CASO O USUÁRIO TENHA SEU SALDO ZERADO
            print("Estamos encerrando o programa...\n")

            break

        system('cls')

    userProfits = userMoney - userMoneyInitial
    totalGames = totalWins + totalDefeats

    system('cls')

except KeyboardInterrupt:
    userProfits = userMoney - userMoneyInitial
    totalGames = totalWins + totalDefeats

finally:
    system('cls')

    print(f"SEU SALDO INICIAL FOI:       R$ {zero_number_left(userMoneyInitial)}")
    print(f"SEU SALDO FINAL FOI:         R$ {zero_number_left(userMoney)}")
    print(f"SEU LUCRO TOTAL FOI:         R$ {zero_number_left(userProfits)}")
    
    if userMoney <= 0:
        print(f"SALDO MÁXIMO ALCANÇADO FOI:  R$ {zero_number_left(maximumMoneyReached)}")
    
    print()
    
    print(f"QUANTIDADE DE JOGOS QUE VOCÊ TEVE FOI:    {totalGames}")
    print(f"QUANTIDADE DE VITÓRIAS QUE VOCÊ TEVE FOI: {totalWins}")
    print(f"QUANTIDADE DE DERROTAS QUE VOCÊ TEVE FOI: {totalDefeats}")

    if userMoney <= 0:
        print(f"QUANTIDADE DE DERROTAS SEGUIDAS FOI:      {totalLossesInaRow}")

    print()
    exit()
