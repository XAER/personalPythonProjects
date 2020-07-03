import random

print("Welcome to Guess The Number!\n")

# Generating random number that the User needs to Guess

print("Generating random number..")
randNum = random.randint(1, 20);
print("\nReady!\n")



def playAgain():
    # If the player whats to play again
    bool = True
    while(bool):
        secondChoice = int(input("Do you want to play again? \n"
                                 "1: Yes\n"
                                 "2: No"))
        if secondChoice == 1:
            startGame()
        elif secondChoice == 0:
            bool = False


# User Playing
def startGame():
    print("You have 20 tries to guess the number generated.")

    b = True

    while b:
        for i in range(20):
            print("Remaining Guesses: " + str(20 - i) + "\n")
            guess = int(input("Guess n. " + str(i + 1) + "\n"))
            if guess == randNum:
                print("You Win!")
                b = False
                break
            elif guess > randNum:
                print(str(guess) + " is too high!\n")
            elif guess < randNum:
                print(str(guess) + " is too low!\n")

            if i == 20:
                b = False

        playAgain()

startGame()