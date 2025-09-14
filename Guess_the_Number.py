# IMPORTANT!!! Please run "Guess the Number 2.py" for direct access to Command Prompt.

# Import the modules
import random
from time import *
from colorama import init
# Initialize colorama
init()
# Download necessary colorama packages
from colorama import Fore, Back, Style

print(Fore.CYAN + '''Welcome to Guess the Number!
''')
# Reset all variables and achievements
achievement1 = False
achievement2 = False
ach = []
achNotEarned = ["1. Dat Smart Guy: Guess a number in 5 guesses or less.", "2. IDK How2Play: Guess a number in 50 guesses or more."]
xp = 0
gameModeBonus = 0

# while True makes it loop forever
while True:
    # The homescreen. Asks the player to type in something.
    # As long as difficultyType is True, the homescreen will appear after the player types something.
    difficultyType = True
    while difficultyType == True:
        print(Style.NORMAL + Fore.CYAN + "=== GAME MODES ===")
        print(Fore.RESET + "Type your difficulty level: " + Fore.BLUE + "Easy, " + Fore.GREEN + "Medium, " + Fore.YELLOW + "Hard, " +\
              Fore.RED + Style.BRIGHT + "Insane" + Fore.RESET + " or " + Fore.RED + Style.DIM + "Extreme" + Style.RESET_ALL + ".")
        print("Or you can" + Fore.YELLOW + " view your achievements by typing Ach" + Fore.RESET + "," + \
              Fore.YELLOW + "view your current total XP by typing XP " + Fore.RESET + "or" + Fore.RED + Style.BRIGHT + " leave by typing Leave" + \
              Style.RESET_ALL + ".")
        print(Style.BRIGHT + Fore.BLUE + "Support " + Style.NORMAL + Fore.YELLOW + "Ukraine!")
        select = input(Style.RESET_ALL)
        # This is the game selection confirmation
        # In these, difficultyType is set to False, breaking out of the while difficultyType == True loop.
        # This prevents the homescreen from appearing during the game
        if select == "Easy":
            print(Fore.BLUE + "You selected Easy!")
            maxNumber = 50
            number = random.randint(1, 50)
            print(Fore.RESET + "I have chosen a number from 1 to 50. See if you can guess what it is!")
            gameModeBonus = 0
            difficultyType = False
        elif select == "Medium":
            print(Fore.BLUE + "You selected Medium!")
            maxNumber = 100
            number = random.randint(1, 100)
            print(Fore.RESET + "I have chosen a number from 1 to 100. See if you can guess what it is!")
            gameModeBonus = 35
            difficultyType = False
        elif select == "Hard":
            print(Fore.BLUE + "You selected Hard!")
            maxNumber = 500
            number = random.randint(1, 500)
            print(Fore.RESET + "I have chosen a number from 1 to 500. See if you can guess what it is!")
            gameModeBonus = 65
            difficultyType = False
        elif select == "Insane":
            print(Fore.BLUE + "You selected Insane!")
            maxNumber = 1000
            number = random.randint(1, 1000)
            print(Fore.RESET + "I have chosen a number from 1 to 1000. See if you can guess what it is!")
            gameModeBonus = 80
            difficultyType = False
        elif select == "Extreme":
            print(Fore.RED + Style.DIM + "You selected Extreme! Don't blame me if your brain overheats and explodes.")
            maxNumber = 20000
            number = random.randint(1, 20000)
            print(Style.RESET_ALL + "I have chosen a number from 1 to 20000. See if you can guess what it is!")
            gameModeBonus = 115
            difficultyType = False
        elif select == "Ach":
            # This shows the player achievements
            print(Fore.YELLOW + "Here are the achievements you have earned:")
            print(ach)
            print("And here are the achievements you have not earned:")
            print(achNotEarned)
        elif select == "XP":
            # This shows the current total XP
            print(Fore.YELLOW + f"Your current total XP is {xp}.")
        elif select == "Leave":
            # Leaves the game
            print(Style.RESET_ALL + Fore.BLUE + "Goodbye. Thank you for playing Guess the Number!")
            sleep(2)
            exit()
        else:
            # Appears when the player types something invalid in the homescreen
            print(Style.NORMAL + Fore.RED + "Sorry, that was an invalid game mode. (Try making the first letter uppercase because we are case sensitive!)")

    # The actual game
    gameOn = True
    guesses = 0
    print(Style.RESET_ALL + "Pick a number.")
    while gameOn == True:
        choice2 = input()
        if str.isdigit(choice2):
            choice = int(choice2)
        else:
            # If you guess something that is not a number, choice is set to "INVALID"
            choice = "INVALID"
        #if type(choice) == int checks if the guess is a number. If it is not, then the program jumps to line 143
        if type(choice) == int:
            if choice == number:
                # Appears when the guess is correct.
                guesses = guesses + 1
                print(f"You are correct! The number I picked was {number}. You guessed it in {guesses} guesses.")
                # Adds the XP. For every incorrect guess, 5 XP is subtracted from 150 XP.
                # For example, you guessed correctly in 9 guesses, so 5×9=45 XP is taken away from 150 XP, so you earn 150-45=105 XP.
                xpToAdd = 150 - ((guesses - 1) * 5)
                if xpToAdd < 0:
                    # Prevents it from adding negative numbers
                    xpToAdd = 0
                if achievement1 == False and guesses <= 5:
                    # Awards achievements
                    sleep(0.5)
                    print("Achievement earned: Dat Smart Guy")
                    print("Bonus 80 XP added!")
                    achievement1 = True
                    xpToAdd = xpToAdd + 80
                    ach.append("1. Dat Smart Guy: Guess a number in 5 guesses or less.")
                    achNotEarned.remove("1. Dat Smart Guy: Guess a number in 5 guesses or less.")
                elif achievement2 == False and guesses >= 50:
                    sleep(0.5)
                    print("Achievement earned: IDK How2Play")
                    print("Bonus 80 XP added!")
                    xpToAdd = xpToAdd + 80
                    ach.append("2. IDK How2Play: Guess a number in 50 guesses or more.")
                    achNotEarned.remove("2. IDK How2Play: Guess a number in 50 guesses or more.")
                    achievement2 = True
                gameOn = False
            elif choice > maxNumber or choice < 1:
                # Runs if the number is invalid
                print("Sorry, that was an invalid number. Please pick a valid number.")
            elif choice > number:
                # Runs if the guess is less than the correct number
                guesses = guesses + 1
                print(f"My number is lesser than {choice}.")
                print("Try picking another number.")
            elif choice < number:
                # Runs if the guess is greater than the correct number
                guesses = guesses + 1
                print(f"My number is  greater than {choice}.")
                print("Try picking another number.")
        else:
            # Runs if the guess is invalid
            print("Sorry, that was an invalid guess. Please try again.")

    if guesses > 31:
        # Does not award any game mode bonuses if it took more than 31 guesses
        gameModeBonus = 0
    # Adds the XP to add and the game mode bonus to the current XP
    xpToAdd = xpToAdd + gameModeBonus
    xp = xp + xpToAdd

    # Prints the game summary
    print("=== GAME SUMMARY ===")
    print(f"Game mode: {select}")
    print(f"Correct number: {number}")
    print(f"Number of guesses: {guesses}")
    print(f"Game Mode Bonus: {gameModeBonus}")
    print(f"XP added: {xpToAdd}")
    print(f"Current total XP: {xp}")
    if guesses > 31:
        # Tells the player why they did not get a game mode bonus
        print("Game Mode Bonus does not apply when your number of guesses goes over 31.")
    print("Do you want to play again? Press ENTER if yes and type n and then press ENTER if no.")
    playAgain = input()
    if playAgain == "n":
        # Runs if the player types "n", breaks out of the while True loop and ends the program
        # But if the player types anything else besides "n", it returns to the top of the while True loop, which turns difficultyType to True. This shows the homescreen
        print(Style.RESET_ALL + Fore.BLUE + "Goodbye. Thank you for playing Guess the Number!")
        sleep(2)
        exit()
