import random
word_database = ["oh hallo", "vallah", "siktirgit", "was geht yallah", "skibidi"] # alle möglichen Wörter
word = random.choice(word_database) # eins der möglichen wörter wird mit random zufällig ausgewählt
guessedWord = ["_"] * len(word) # damit man das wort nicht direkt sieht, wird für jeden buchstaben ein "_" eingesetzt
attempts = 10

while attempts > 0:
    print("\nCurrent word: " + "".join(guessedWord)) # \n = zeilenumbruch, .join() verbindet die Buchstaben in guessedWord zu einem String
    guess = input("Guess a letter: ").lower() # .lower() function macht den eingegebenen Buchstaben zu einem kleinen Buchstaben also A zu a
    
    if guess in word:   #   die for loop checkt jeden buchstaben des wortes und schaut so an welcher stelle der buchstabe erraten wurde
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: " + str(attempts)) # attempts muss hier in einen string gewandelt werden da es eigentlich ein integer ist
    
    if "_" not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break
    elif attempts == 0 and "_" in guessedWord:
        print("\nYou\'ve run out of attempts! The word was: " + word)
    

    

