import random

print("Welcome to Guess The Number!\n")

# Generating random number that the User needs to Guess

print("Generating random number..")
randNum = random.randint(1, 20);
print("\nReady!\n")

# User Playing

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



