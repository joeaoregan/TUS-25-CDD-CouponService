# A00258304

from random import randint, seed
seed(1)

random_number = randint(1, 100)

for attempt in range(1, 11):
    player_guess = int(input(f"Enter your guess: "))

    if player_guess > random_number:
        print("Too high")
    elif player_guess < random_number:
        print("Too low")
    else:
        print(f"You win, you got it in {attempt} guesses")
        break
else:
    print(f"You lose, the number was {random_number}")
