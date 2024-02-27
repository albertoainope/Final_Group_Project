from testing import top_10_words
def play_game(top_words):
    """
    Play the word guessing game
    :param top_words: list of top words to guess
    """
    print("Welcome to the word guessing game! Write 'exit' to quit the game.")
    print("Try to guess the words longer than 5 characters from the text.")
    guessed_words = []
    count = 0
    while len(guessed_words) < len(top_words):
        guess = input("Enter a word: ").lower()
        if guess == "exit":
            raise ValueError
        if guess in top_words and guess not in guessed_words:
            guessed_words.append(guess)
            count += 1
            print(f"Correct! You have guessed the following words: {guessed_words}")
            print(f"You are missing {10-count} words")
        else:
            print("Incorrect. Try again!")
    print("Congratulations! You guessed all the words!")

try:
    play_game(top_10_words("williamson.txt"))
except ValueError:
    print("GAME OVER")