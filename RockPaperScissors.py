import random

print("Welcome to Rock, Paper, Scissors vs CPU!")

b = True


def startGame():

    gameStatus = True
    playerScore = 0
    cpuScore = 0

    # 1. Rock
    # 2. Paper
    # 3. Scissors

    while gameStatus:
        # 3 Rounds
        for i in range(3):
            cpuMove = random.randint(1, 3)
            playerMove = input("Choose a move:\n"
                               "1. Rock\n"
                               "2. Paper\n"
                               "3. Scissors\n")

            if cpuMove == 1:
                cpuMoveString = "Rock"
            elif cpuMove == 2:
                cpuMoveString = "Paper"
            elif cpuMove == 3:
                cpuMoveString = "Scissors"

            if playerMove == 1:
                playerMoveString = "Rock"
            elif playerMove == 2:
                playerMoveString = "Paper"
            elif playerMove == 3:
                playerMoveString = "Scissors"

            if playerMove == cpuMove:
                print("CPU: " + cpuMoveString + "\n"
                      "Your Move: " + playerMoveString + "\n"
                      "Draw.")
            elif playerMove == 1 & playerMove == 3:
                print("CPU: " + cpuMoveString + "\n"
                      "Your Move: " + playerMoveString + "\n" +
                      "Player Wins!")
                ++playerScore

            playAgain()



while(b):
    print("Insert 1 to Play \n Insert 0 to Quit\n")
    userChoice = int(input("||:"))
    if userChoice == 1:
        # Start Game
        startGame()
    elif userChoice == 0:
        b = False

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
