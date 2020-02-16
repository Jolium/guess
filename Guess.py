from random import randint
from time import sleep


def game_start():
    """Choosing who plays first"""
    player = randint(0, 1)
    random_number = random_numb()
    if player == 0:
        bot_guess(random_number)
    if player == 1:
        player_guess(random_number)


def random_numb():
    """Range of numbers and random number selection"""
    low_number = 1
    high_number = 20
    random_number = randint(low_number, high_number)

    print("\n--------------------------")
    print("---  GUESS THE NUMBER  ---")
    print("--------------------------")
    print(f"-----  from {low_number} to {high_number}  -----")
    print("--------------------------\n")

    with open('python_range.txt', 'w') as f:
        f.write(f"{low_number}\n{high_number}")
    return random_number


def player_guess(random_number):
    """Number guessed by player"""
    while True:
        values = open('python_range.txt').read().splitlines()
#        print(f"[{random_number}] low >= {values[0]} ; high <= {values[1]}")
        try:
            player_number = int(input("My guess is: "))
            if int(values[0]) <= player_number <= int(values[1]):
                if player_number == random_number:
                    print("Congratulations, good job!")
                    play_again()
                elif player_number > random_number:
                    print("Too high!\n==========================\nPython, it is your turn...")
                    sleep(1)
                    if player_number <= int(values[1]):
                        save_low_high_values(low=int(values[0]), high=player_number - 1)
                    bot_guess(random_number)
                elif player_number < random_number:
                    print("Too low!\n==========================\nPython, it is your turn...")
                    sleep(1)
                    if player_number >= int(values[0]):
                        save_low_high_values(low=player_number + 1, high=int(values[1]))
                    bot_guess(random_number)
                return player_number
            else:
                print("Not valid answer!\n")
                player_guess(random_number)
        except ValueError:
            print("Not valid answer!\n")
            player_guess(random_number)


def save_low_high_values(low, high):
    """Save the low and high values to limit bot range"""
    values = open('python_range.txt').read().splitlines()

    if int(values[0]) >= low:
        low = int(values[0])
    elif int(values[1]) <= high:
        high = int(values[1])

    with open('python_range.txt', 'w') as f:
        f.write(f"{low}\n{high}")


def bot_guess(random_number):
    """Number guessed by bot"""
    while True:
        values = open('python_range.txt').read().splitlines()
        low_value = int(values[0])
        high_value = int(values[1])
#        print(f"[{random_number}]  low >= {low_value} ; high <= {high_value}")
        python_number = randint(low_value, high_value)

        print(f"Python guess is: {python_number}")

        if python_number == random_number:
            print(f"You lost, {python_number} was right!")
            play_again()
        elif python_number > random_number:
            print("Too high!")
            sleep(1)
            print("==========================\nPlayer, it is your turn...")
            save_low_high_values(low=int(values[0]), high=python_number - 1)
            player_guess(random_number)
        elif python_number < random_number:
            print("Too low!")
            sleep(1)
            print("==========================\nPlayer, it is your turn...")
            save_low_high_values(low=python_number + 1, high=int(values[1]))
            player_guess(random_number)


def play_again():
    """Asking at the end if player wants to play again."""
    print("==========================\nDo you want to play again?")
    answer = input("y / n : ")

    if answer == 'y':
        game_start()
    elif answer == 'n':
        print("\n= Thank you for playing! =")
        exit()
    else:
        play_again()


game_start()
