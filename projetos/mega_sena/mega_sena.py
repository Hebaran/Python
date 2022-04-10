__import__('os').system('cls')

print('\033[31m', end="")
print('--------------------------------------')
print('|         JOGUE NA MEGA SENA         |')
print('--------------------------------------')
print('\033[m')

while True:
    last_sort = []
    
    last_sort_pass = str(input('Deseja inserir o resultado da ultima Mega-Sena? [S/N] ')).strip().upper()
    
    if last_sort_pass not in 'SN':
        print('\n\033[31mDigite apenas S ou N\033[m')
    
    else:
        if last_sort_pass == 'S':
            last_sort_backup = str(input('Digite os números do último sorteio separados por ";": ')).strip().split(';')
            
            for winning_number in last_sort_backup:
                last_sort.append(f'({winning_number})')

        break

while True:    
    games_amount = int(input('Quantos jogos você quer sortear: '))
    
    if games_amount >= 100:
        print('\n\033[31mDa uma segurada aí irmão, pra que isso tudo?\033[m')
    
    else:
        while True:
            numbers_amount = int(input('Quantos números você quer sortear: '))
            
            if numbers_amount < 6 or numbers_amount > 15:
                print('\n\033[31mValor inválido, só posso sortear de 6 a 15 números\033[m')
            
            else:
                break
        
        break

print(f'\n========= SORTEANDO {games_amount:02} JOGOS =========\n')

for c in range(0, games_amount):
    sort_numbers = []
    number_confirmation = []
    
    while True:
        random_number = str(__import__('random').randint(1, 60))
        
        if random_number not in number_confirmation:
            number_confirmation.append(random_number)
            sort_numbers.append('(' + random_number.zfill(2) + ')')
                    
        if len(sort_numbers) >= numbers_amount:
            break
        
    sort_numbers.sort()
    
    print(f'\033[34mJogo {c + 1:02}:\033[m ', end="")
    
    count = 0
    
    for number in sort_numbers:
        count += 1
        
        color = '\033[31m' if number in last_sort else '\033[32m'
        
        if count != len(sort_numbers):
            print(f'{color}{number}\033[m', end=" ") 
            
        else:
            print(f'{color}{number}\033[m')
            
    print()
