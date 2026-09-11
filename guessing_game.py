import random

print("===== NUMBER GUESSING GAME =====")
print("1. Easy - 10 guesses")
print("2. Hard - 5 guesses")

level = input("Choose your level (1 or 2): ")

if level == "1":
    max_guesses = 10
    print("You chose Easy level!")
elif level == "2":
    max_guesses = 5
    print("You chose Hard level!")
else:
    print("Invalid choice!")
    max_guesses = 0

if max_guesses > 0:
    number = random.randint(1, 100)
    guesses = 0
    won = False

    print("I have chosen a number between 1 and 100.")

    while guesses < max_guesses:
        guess = int(input("Enter your guess: "))
        guesses = guesses + 1

        if guess == number:
            print("Congratulations! You guessed the number!")
            print("You used", guesses, "guesses.")
            won = True
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        print("Guesses left:", max_guesses - guesses)

    if won == False:
        print("Game Over!")
        print("The correct number was:", number)