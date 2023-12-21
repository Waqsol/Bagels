import random

secret_number = str(random.randint(100, 999))
print('Welcome to the game *Bagles*! You have 10 tries to guess a three-digit number')
attempts = 0

while attempts < 10:
    print('Write your three-digit number')
    check_correct_number = 0

    while check_correct_number != 1:
        input_number = input()
        if len(input_number) != 3:
            print('Your number is not made up of three numbers, please try again')
        elif not input_number.isdigit():
            print('Your number is not made up of numbers, please try again')
        else:
            check_correct_number = 1
    check_correct_number = 0

    for i in range(3):
        if input_number[i] == secret_number[i]:
            print('Fermi!')
            break
        elif input_number[i] in secret_number:
            print('Pico!')
            break
    else:
        print('Bagels!')
    if input_number == secret_number:
        print('Congratulations, you guessed the number!')
        break
    attempts += 1
    print(f'You are left with {10 - attempts} attempts')
    print()
