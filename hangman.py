x = input("Select an option:\n1. Play the game\n2. Quit\n")

while x != "2":
    y = input("\nSelect a category:\n1: Fruits\n2: Colours\n3: Shapes\n")
    print("""
    _____
    |    |
    |
    |
    |
    |__""")
    import random

    if y == "1":
        a = ["apple", "banana", "orange"]
        word = random.choice(a)
    elif y == "2":
        b = ["black", "blue", "pink"]
        word = random.choice(b)
    else:
        c = ["square", "rectange", "circle"]
        word = random.choice(c)

    final = ["_"] * len(word)

    print(final)
    print("Let's play hangman!")
    wrong = 0
    guess_list = []

    while final != list(word) and wrong != 8:
        index = 0
        guess = input("\nEnter the guessed character\n")
        guess_list.append(guess)
        if guess == "":
            print("Please enter a character!")
        elif len(guess) > 1:
            print("Enter one character at a time!")
        else:
            if guess not in word:
                wrong = wrong + 1
                print("\nYou have tried the below characters\n", guess_list)
            else:
                for e in word:
                    if guess == e:
                        final[index] = e
                    index += 1
                print("\nYou have tried the below characters\n", guess_list)

        print("\nWord:\n", final)
        print("\nNumber of wrong guesses = ", wrong)
        if wrong == 1:
            print("""
            _____
            |    |
            |    o
            |
            |                
            |
            |__


            """)
        if wrong == 2:
            print("""
            _____
            |    |
            |    o
            |    |
            |                
            |
            |__


            """)

        if wrong == 3:
            print("""
            _____
            |    |
            |    o
            |   /|
            |                
            |
            |__


            """)

        if wrong == 4:
            print("""
            _____
            |    |
            |    o
            |   /|\
            |                
            |
            |__


            """)

        if wrong == 5:
            print("""
            _____
            |    |
            |    o
            |   /|\
            |    |
            |                
            |__


            """)
        if wrong == 6:
            print("""
             _____
            |    |
            |    o
            |   /|\
            |    |
            |   /          
            |__


            """)
        if wrong == 7:
            print("""
             _____
            |    |
            |    o
            |   /|\
            |    |
            |   / \         
            |__


            """)
            print("Oh no! You've lost!")
            x = input("Select an option:\n1. Play the game\n2. Quit\n")
            wrong = 8
        if (final == list(word)):
            print("Congratulations!\nYou have won!\n")
            x = input("Select an option:\n1. Play the game\n2. Quit\n")
print("Game Over!")