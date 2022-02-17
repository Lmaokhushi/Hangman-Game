import random

def hangman():
    words = random.choice(["hello", "serene", "superman", "selection", "yonsei", "windows", "doors", "india", "game", "haikyuu"])
    letters = "abcdefghijklmnopqrstuvwxyz"
    attempts = 10
    guess= ''

    while len(words) > 0:
        main = ""
        missed = 0

        for letter in words:
            if letter in guess:
                main = main + letter
            else: 
                main = main + "_" + " "
        if main == words:
            print(main)
            print("Yayy, you win!!")
            break

        print("Guess the word:" , main)
        guessmade = input()

        if guessmade in letters:
            guess = guess + guessmade
        else:
            print("Enter a valid letter:")
            guessmade = input()
        
        if guessmade not in words:
            attempts = attempts - 1
            if attempts == 9:
                print("9 attempts left")
                print("  --------  ")
            if attempts == 8:
                print("8 attempts left")
                print("  --------  ")
                print("     O      ")
            if attempts == 7:
                print("7 attempts left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if attempts == 6:
                print("6 attempts left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if attempts == 5:
                print("5 attempts left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if attempts == 4:
                print("4 attempts left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if attempts == 3:
                print("3 attempts left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if attempts == 2:
                print("2 attempts left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if attempts == 1:
                print("1 attempts left")
                print("Last breaths counting!!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if attempts == 0:
                print("You lost!!")
                print("You let a kind man die :(")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

print("try to guess the word in less than 10 attempts:")
hangman()
 

         
