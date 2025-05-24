import streamlit as st
import random

words = ["Pakistan", "Book", "Random", "Justice", "Six", "Manchester"]

def get_word():
    word = random.choice(words)
    return word.upper()

def display_hangman(tries):
    stages = [
        # Final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # Head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # Head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # Head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    st.write("Let's play Hangman!")
    st.text(display_hangman(tries))
    st.write(word_completion)
    
    while not guessed and tries > 0:
        guess = st.text_input("Guess a letter or the whole word:").upper()
        
        if guess in guessed_letters:
            st.warning("You already guessed that letter!")
        elif len(guess) == 1 and guess.isalpha():
            if guess in word:
                st.success(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
            else:
                st.error(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = True
                word_completion = word
            else:
                st.error(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
        else:
            st.warning("Not a valid guess.")
        
        st.text(display_hangman(tries))
        st.write(word_completion)
        st.write(f"Guessed letters: {', '.join(guessed_letters)}")
    
    if guessed:
        st.success("Congratulations! You guessed the word!")
    else:
        st.error(f"Sorry, you ran out of tries. The word was {word}.")

def main():
    st.title("Hangman Game")
    word = get_word()
    play(word)

if __name__ == "__main__":
    main()