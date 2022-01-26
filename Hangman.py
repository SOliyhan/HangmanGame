

from words import word_list
import random

def get_valid_word():
    # getting the valid list of words from words.py

    word= random.choice(word_list)      #randomly choose something from words
    return word.lower()


def game(word):
    # game fuction to dusplay progress and result of the player

    try:
        word= random.choice(word_list)
        turns=6
        guessed=False
        guessed_letters=[]
        guessed_words=[]
        full_word= "_" * len(word)
        print('Let\'s play hangman!!!')
        print('Try to guess the word in 6 attempts')
        print(f"Hint: length of the word is '{len(word)}'")
        print(hangman(turns))
        print(f"Word: {full_word}\n")

        while not guessed and turns>0:

            guess= input('Please guess a letter or word: ').lower()
            
            if len(guess)==1 and guess.isalpha():
                # if a letter is guessed by user

                if guess in guessed_letters:
                    print(f'You already guessed the letter {guess}')
                    print(f"Attempts left: {turns}")
                elif guess not in word:
                    print(f"Sorry, '{guess}' is not in the word.")
                    turns-=1
                    guessed_letters.append(guess)
                    print(f"Attempts left: {turns}")
                else:
                    print(f"Good job '{guess}' is in the word.")
                    print(f"Attempts left: {turns}")
                    guessed_letters.append(guess)
                    list_words= list(full_word)
                    indices= [i for i,letter in enumerate(word) if letter==guess]
                    for index in indices:
                        list_words[index]=guess
                    full_word="".join(list_words)
                    if "_" not in full_word:
                        guessed=True

            elif len(guess)==len(word) and guess.isalpha():
                # if entire word or partial word is guessed by user

                if guess in guessed_words:
                    print(f"You already guessed the word '{guess}' Guess again...")
                    print(f"Attempts left: {turns}")
                elif guess!=word:
                    print(f"'{guess}' is not in the word")
                    turns-=1
                    guessed_words.append(guess)
                    print(f"Attempts left: {turns}")
                else:
                    guessed=True
                    full_word=word

            else:
                print("Invalid guess.. Try again!!")
                print(f"Attempts left: {turns}")
            print(hangman(turns))
            print(f"Word: {full_word}\n")
        if guessed:
            print("Congrats you guessed the word! You Won the Hangman game!!...$$$")
        else:
            print(f"You ran out of attempts. The word was '{word}'. Try next time...good luck!")

    except Exception as e:
        print('Exception occurs as ',e)

def hangman(turns):
    #contains a list that shows the state of hanging man after certain guesses

    hanging_man=["""
                    ----------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    -
                """,
                """
                    ----------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / 
                    -
                """, 
                """
                    ----------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      
                    -
                """,
                """
                    ----------
                    |       |
                    |       O
                    |      \\|
                    |       |
                    |      
                    -
                """,
                """
                    ----------
                    |       |
                    |       O
                    |       |
                    |       |
                    |      
                    -
                """,
                """
                    ----------
                    |       |
                    |       O
                    |     
                    |       
                    |      
                    -
                """,
                """
                    ----------
                    |       |
                    |
                    |     
                    |       
                    |      
                    -
                """]
    return hanging_man[turns]

def main():
    name= input("Enter your Name: ").capitalize()
    print(f'Hello {name}!! Welcome to Hangman Game')
    print('--'*15)
    word=get_valid_word()
    game(word)
    while input('Play Again... (Y/N): ').upper()=='Y':
        word=get_valid_word()
        game(word)

if __name__=="__main__":
    main()

