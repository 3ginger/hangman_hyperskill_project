import random

langs = ['python', 'java', 'kotlin', 'javascript']
valid_letters = list('abcdefghijklmnopqrstuvwxyz')
NUM_TRIES = 8

def getPublicWord(word, letters):
    public_word = ''
    for letter in word:
        if letter in letters:
            public_word += letter
        else:
            public_word += "-"
    return public_word

def isWordGuessed(word, letters):
    return '-' not in getPublicWord(word, letters)

def play_game():
    word = langs[random.randint(0, len(langs) - 1)]
    letters = []
    num_tries = NUM_TRIES

    while num_tries > 0:
        print()
        print(getPublicWord(word, letters))
        next_letter = input('Input a letter: ')

        if len(next_letter) > 1:
            print('You should print a single letter')
            continue
        
        if next_letter not in valid_letters:
            print('It is not an ASCII lowercase letter')
            continue

        if next_letter in letters:
            print("You already typed this letter")
            continue

        if next_letter not in word:
            print("No such letter in the word")
            letters.append(next_letter)
            num_tries -= 1
            continue

        letters.append(next_letter)
        if isWordGuessed(word, letters):
            print("You guessed the word {}!".format(word))
            print("You survived!")
            print()
            break

    if num_tries == 0:
        print("You are hanged!")
        print()
    
def select_mode():
    mode = input('Type "play" to play the game, "exit" to quit: ')
    if mode == 'play':
        play_game()
    elif mode == 'exit':
        return

print("H A N G M A N")
select_mode()
