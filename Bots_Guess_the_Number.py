# Import modules and welcome the user
import random
import time
print("Welcome to Bots Guess The Number!")
# Set bot win comment lists
randy_comments = ["YAY CORRECT! SEE, I TOLD YOU I WOULD GUESS IT!", ":)", 
                   "YAAAAAAAAAASSSSS!!!!!11!1!1! CORRECT CORRECT!!!!!", 
                   "GG YAY NOW DO IT AGAIN?", 
                   "YIPPEE!!! ME SO HAPPEE!!! ME WANT MANGOEE!!!", 
                  "MY STRATEGY IS THE BEST! MY STRATEGY IS THE BEST!"]
iterator_comments = ["Wʜᴏᴏᴘ-ᴡʜᴏᴏᴘ! I ᴡᴏɴ!", "Yᴇᴀʜ! I ᴛᴏʟᴅ ʏᴏᴜ ɪᴛ ᴡᴏʀᴋꜱ!", 
                     "Tʜɪꜱ ꜱᴛʀᴀᴛᴇɢʏ ɪꜱ ꜱᴏ ᴍᴜᴄʜ ʙᴇᴛᴛᴇʀ ᴛʜᴀɴ Rᴀɴᴅʏ'ꜱ, ᴅᴏɴ'ᴛ ʏᴏᴜ ᴀɢʀᴇᴇ?", 
                     "ITᴇRᴀTᴏʀ ɪɴ ᴅᴀ Hᴏᴜꜱᴇ!!!", "Iᴛᴇʀᴀᴛɪᴏɴ ꜱᴜʀᴇ ɪꜱ ᴛʜᴇ ʙᴇꜱᴛ ꜱᴛʀᴀᴛᴇɢʏ ᴇᴠᴇʀ!", 
                     "Tʜᴀᴛ. Wᴀꜱ. Aᴡᴇꜱᴏᴍᴇ!"]
e15step_comments = ["𝚆𝚒𝚗𝚗𝚒𝚗𝚐 𝚎𝚟𝚎𝚛𝚢 𝚐𝚊𝚖𝚎, 𝟷𝟻 𝚜𝚝𝚎𝚙𝚜 𝚊𝚝 𝚊 𝚝𝚒𝚖𝚎.", 
                    "𝙾𝚑𝚑𝚑𝚑 𝚢𝚎𝚊𝚑, 𝙸'𝚖 𝚝𝚑𝚎 𝙶𝚞𝚎𝚜𝚜𝚒𝚗𝚐 𝙼𝚊𝚜𝚝𝚎𝚛!", 
                    "𝟷𝟻𝚂𝚝𝚎𝚙 𝚒𝚜 𝚝𝚑𝚎 𝙱𝙴𝚂𝚃 𝚘𝚏 𝚝𝚑𝚎 𝙱𝙴𝚂𝚃!", "𝙽𝚘𝚠 𝚠𝚑𝚎𝚛𝚎'𝚜 𝚖𝚢 𝚙𝚛𝚒𝚣𝚎?", 
                    "𝟹 𝚌𝚑𝚎𝚎𝚛𝚜 𝚏𝚘𝚛 𝙼𝙴! 𝟷𝟻𝚂𝚝𝚎𝚙! 𝟷𝟻𝚂𝚝𝚎𝚙! 𝟷𝟻𝚂𝚝𝚎𝚙!", ]
averager_comments = ["𝘞𝘢𝘪𝘵... 𝘐 𝘸𝘰𝘯???! 𝘕𝘖 𝘞𝘈𝘠!", "𝘛𝘩𝘢𝘵 𝘸𝘢𝘴 𝘧𝘢𝘴𝘵... 𝘴𝘰 𝘧𝘢𝘴𝘵!", 
                     "𝘏𝘰𝘸 𝘥𝘪𝘥 𝘐—?!", 
                     "𝘛𝘩𝘢𝘯𝘬𝘴 𝘵𝘰 𝘮𝘺 𝘤𝘳𝘦𝘢𝘵𝘰𝘳, 𝘱𝘭𝘻4𝘹, 𝘧𝘰𝘳 𝘨𝘪𝘧𝘵𝘪𝘯𝘨 𝘮𝘦 𝘸𝘪𝘵𝘩 𝘴𝘶𝘤𝘩 𝘢𝘯 𝘦𝘹𝘤𝘦𝘭𝘭𝘦𝘯𝘵 𝘴𝘵𝘳𝘢𝘵𝘦𝘨𝘺.", 
                     "𝘔𝘺 𝘰𝘸𝘯 𝘴𝘵𝘳𝘢𝘵𝘦𝘨𝘺 𝘢𝘮𝘢𝘻𝘦𝘴 𝘮𝘦..."]

#So this is the main part
while True:
    # Now the user's gotta pick a difficulty, or pick a random one
    while True:
        print("Type a difficulty level for the bot: Easy, Medium, Hard, Insane or Extreme, or type r to pick a random one.")
        difficulty = input()
        # The difficulties list is for the random difficulty picker
        difficulties = ["easy", "medium", "hard", "insane", "extreme"]
        # The user need not worry about case sensitivity, as that's got it all sorted out using the .lower() method :D
        if difficulty.lower() == "r":
            difficulty = difficulties[random.randint(0, 4)]
        if difficulty.lower() == "easy":
            print("You selected Easy! Now type a number between 1 and 50, or type r to pick a random number:")
            maxnum = 50
            break
        elif difficulty.lower() == "medium":
            print("You selected Medium! Now type a number between 1 and 100, or type r to pick a random number:")
            maxnum = 100
            break
        elif difficulty.lower() == "hard":
            print("You selected Hard! Now type a number between 1 and 500, or type r to pick a random number:")
            maxnum = 500
            break
        elif difficulty.lower() == "insane":
            print("You selected Insane! Now type a number between 1 and 1000, or type r to pick a random number:")
            maxnum = 1000
            break
        elif difficulty.lower() == "extreme":
            print('''You selected Extreme! I hope the bots don't take 342 novemquinquagintillion millenia to solve this...
Now type a number between 1 and 20000, or type r to pick a random number:''')
            maxnum = 20000
            break
        else:
            print(f"I have no idea what {difficulty} even is. Can you enter something valid?")
    # Now the user's gotta type a number
    while True:
        try:
            number = input()
            if number.lower() == "r":
                number = random.randint(1, maxnum)
                # Has to convert to a string so the .isnumeric() works
                number = str(number)
            if number.isnumeric():
                if int(number) > maxnum or int(number) < 1:
                    print(f"I said between 1 and {maxnum}. So please stick within the range.")
                else:
                    number = int(number)
                    print(f"You selected {number}!")
                    break
            else:
                if number[0] == "-":
                    print(f"I said between 1 and {maxnum}. So please stick within the range.")
                else:
                    print("Uhh... the number you entered couldn't be converted into an integer. Can you please type something valid?")
        except:
            print("A-whoops... something went wrong. Please try again.")
    
    # Then it's time to pick a bot
    print('''Now select your bot:
Name       Description
Randy    : Picks totally random numbers and hopes he lucks out and gets it
           correct.
Iterator : Brute-forces the number (that means tries every single number
           from 1).
15Step   : Guesses every 15th number (15, 30, 45 and so on). When it
           detects that the number is lower than its guess, it guesses every
           number in that range.
Averager : Does the usual method: guessing the number most in the middle.
Type r to pick a random bot.
Feel free to add your own bots with different strategies!''')
    while True:
        # bots list is for the random bot picker
        bots = ["randy", "iterator", "15step", "averager"]
        bot = input()
        bot = bot.lower()
        if bot.lower() == "r":
            bot = bots[random.randint(0, 3)]
        if bot.lower() == "randy":
            print("You selected Randy!")
            print("HELLO, USER! I AM RANDY. NO MATTER WHAT NUMBER YOU PICK, I WILL ALWAYS GUESS IT. I WILL CONQUER THIS GAME WITH MY STRATEGY! I'M READY. BRING IT ON!")
            print("Ooh, confidence! Well, we'll see about that. Good luck!")
            break
        elif bot.lower() == "iterator":
            print("You selected Iterator!")
            print("H​​🇪​​🇱​​🇱​​🇴​, ​I🇹​​🇪​​🇷​​🇦​​🇹​​🇴​​🇷​ ​🇭​​🇪​​🇷​​🇪​! ​Y​​🇴​​🇺​ ​🇰​​🇳​​🇴​​🇼​ ​🇹​​🇭​​🇦​​🇹​ ​🇧​​🇴​​🇹​ ​🇼​​🇭​​🇮​​🇨​​🇭​ ​🇵​​🇮​​🇨​​🇰​​🇸​ ​🇳​​🇺​​🇲​​🇧​​🇪​​🇷​​🇸​ ​🇦​​🇹​ ​🇷​​🇦​​🇳​​🇩​​🇴​​🇲​? ​P​​🇫​​🇫​​🇫​​🇹​, ​🇼​​🇭​​🇦​​🇹​ ​🇦​ ​🇩​​🇺​​🇲​​🇧​ ​🇸​​🇹​​🇷​​🇦​​🇹​​🇪​​🇬​​🇾​. ​M​​🇾​ ​🇴​​🇳​​🇪​ ​🇮​​🇸​ ​🇧​​🇪​​🇹​​🇹​​🇪​​🇷​, ​🇼​​🇦​​🇾​ ​🇧​​🇪​​🇹​​🇹​​🇪​​🇷​. ​I ​🇼​​🇮​​🇱​​🇱​ ​🇧​​🇪​​🇦​​🇹​ ​🇹​​🇭​​🇮​​🇸​ ​🇬​​🇦​​🇲​​🇪​ ​🇫​​🇴​​🇷​ ​🇸​​🇺​​🇷​​🇪​! ​L​​🇪​​🇹​'​🇸​ ​🇬​​🇴​!")
            print("Hmm... I'm not so sure about that... but I guess it's worth a try! Wish you luck!")
            break
        elif bot.lower() == "15step":
            print("You selected 15Step!")
            print("𝙷𝚒, 𝚖𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜 𝟷𝟻𝚂𝚝𝚎𝚙! 𝙸 𝚑𝚊𝚟𝚎 𝚊 𝚜𝚎𝚌𝚛𝚎𝚝 𝚠𝚎𝚊𝚙𝚘𝚗: 𝚖𝚢 𝚝𝚛𝚒𝚎𝚍-𝚊𝚗𝚍-𝚝𝚎𝚜𝚝𝚎𝚍 𝚜𝚝𝚛𝚊𝚝𝚎𝚐𝚢. 𝙸𝚝 𝚠𝚘𝚛𝚔𝚜 𝚠𝚎𝚕𝚕 — 𝚟𝚎𝚛𝚢 𝚠𝚎𝚕𝚕. 𝙸𝚝'𝚜 𝚝𝚑𝚎 𝚋𝚎𝚜𝚝 𝚜𝚝𝚛𝚊𝚝𝚎𝚐𝚢 𝚘𝚏 𝚊𝚕𝚕 𝚝𝚒𝚖𝚎! 𝙱𝚛𝚎𝚊𝚔 𝚊 𝚕𝚎𝚐 — 𝚝𝚘 𝚖𝚎 𝚘𝚏 𝚌𝚘𝚞𝚛𝚜𝚎!")
            print("Enthusiastic, isn't he? Once again, break a leg! Get ready, 15Step, for the game is about to commence!")
            break
        elif bot.lower() == "averager":
            print("You selected Averager!")
            print("𝘏𝘪 𝘵𝘩𝘦𝘳𝘦, 𝘐'𝘮 𝘈𝘷𝘦𝘳𝘢𝘨𝘦𝘳. 𝘐 𝘥𝘰𝘯'𝘵 𝘸𝘢𝘯𝘵 𝘵𝘰 𝘣𝘳𝘢𝘨, 𝘣𝘶𝘵 𝘐 𝘩𝘢𝘷𝘦 𝘵𝘩𝘪𝘴 𝘮𝘦𝘵𝘩𝘰𝘥 𝘰𝘧 𝘣𝘦𝘢𝘵𝘪𝘯𝘨 𝘵𝘩𝘪𝘴 𝘨𝘢𝘮𝘦. 𝘐𝘵'𝘴 𝘳𝘦𝘢𝘭𝘭𝘺 𝘦𝘧𝘧𝘦𝘤𝘵𝘪𝘷𝘦. 𝘐'𝘷𝘦 𝘵𝘳𝘪𝘦𝘥 𝘪𝘵 𝘰𝘶𝘵 𝘮𝘢𝘯𝘺 𝘵𝘪𝘮𝘦𝘴 — 𝘢𝘯𝘥 𝘪𝘵 𝘩𝘦𝘭𝘱𝘦𝘥 𝘮𝘦 𝘤𝘰𝘯𝘲𝘶𝘦𝘳 𝘨𝘢𝘮𝘦𝘴 𝘸𝘪𝘵𝘩𝘰𝘶𝘵 𝘧𝘢𝘪𝘭. 𝘈𝘯𝘺𝘸𝘢𝘺𝘴, 𝘸𝘪𝘴𝘩 𝘮𝘦 𝘭𝘶𝘤𝘬!")
            print("Thank you so much, Averager, for being modest. Hope you win!")
            break
        else:
            print(f"Who in the world is {bot}? Please type an existing bot name.")
    # Reset all neccessary variables, make neccessary preparations for bots
    guesses = 1
    guess = 0
    feedback = "greater"
    maxrange = maxnum
    minrange = 1
    print("Alright, let's begin! 3... 2... 1... GO!")
    time.sleep(0.5)
    while True:
        if bot == "randy":
            guess = random.randint(1, maxnum)
        elif bot == "iterator":
            guess += 1
        elif bot == "15step":
            if feedback == "greater":
                guess += 15
                if guess > maxnum:
                    guess = maxnum
            elif feedback == "smaller":
                guess -= 1
        elif bot == "averager":
            if guesses != 1:
                if feedback == "greater":
                    minrange = guess + 1
                if feedback == "smaller":
                    maxrange = guess - 1
            guess = round((maxrange + minrange) / 2)
        # Code for guess checking
        print(f"Guess #{guesses}: {guess}")
        if guess == number:
            print(f"{guess} is correct!")
            if bot == "randy":
                print(randy_comments[random.randint(0, 5)])
            elif bot == "iterator":
                print(iterator_comments[random.randint(0, 5)])
            elif bot == "15step":
                print(e15step_comments[random.randint(0, 4)])
            elif bot == "averager":
                print(averager_comments[random.randint(0, 4)])
            break
        elif guess > number:
            print(f"The answer is smaller than {guess}.")
            guesses += 1
            feedback = "smaller"
        elif guess < number:
            print(f"The answer is greater than {guess}.")
            guesses += 1
            feedback = "greater"
    # Game summary
    print(f'''GAME SUMMARY
Correct number: {number}
Bot: {bot.title()}
Number of guesses: {guesses}
Press enter to return to the homepage.''')
    input()

