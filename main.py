from testing import top_10_words
#I want to use top_10_words function to make the user input a word, and if it is in the top 10 words, print the word and ask for input again until the user inputs all words in the top 10
try:
    def play_game(top_words):
        """
        Play the word guessing game
        :param top_words: list of top words to guess
        """
        print("Welcome to the word guessing game!")
        print("Try to guess the words longer than 5 characters from the text.")
        guessed_words = set()
        while len(guessed_words) < len(top_words):
            guess = input("Enter a word: ").lower()
            if guess in top_words and guess not in guessed_words:
                print("Correct!")
                guessed_words.add(guess)
            else:
                print("Incorrect. Try again!")
        print("Congratulations! You guessed all the words!")
    play_game(top_10_words("williamson.txt"))

except ValueError:
    print("Please put a word")

