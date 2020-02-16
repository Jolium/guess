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
            else:
                print("Not valid answer!\n")
                player_guess(random_number)
                return player_number
        except ValueError:
            print("Not valid answer!\n")
            player_guess(random_number)


player_guess(10)
