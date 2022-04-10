from random import randint

user_choice = str(input('+roll ')).strip().lower()

separate_numbers = user_choice.split('d')
separate_numbers[0] = int(separate_numbers[0])
separate_numbers[1] = int(separate_numbers[1])

all_rolls = []
sum_rolls = count = 0

for roll in range(0, separate_numbers[0]):
    all_rolls.append(randint(0, separate_numbers[1]))

for number in all_rolls:
    sum_rolls += number

print(f'\n🎲 | @user Rolou {separate_numbers[1]}... e conseguiu {sum_rolls}!')
print(f'🤓 | {sum_rolls} » ', end="")

for item in all_rolls:
    count += 1
    print(item, end=" + ") if count != len(all_rolls) else print(item)
