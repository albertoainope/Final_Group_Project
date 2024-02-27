def top_10_words(file_name):
    """
    This function will return the top 10 most repeated words longer than 4 characters in a text file
    :param file_name: the name of the file
    :return: list of top 10 words longer than 4 characters
    """
    frequency = {}
    punctuation = "(,)'.!?\n"
    with open(file_name, "r") as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p, "")
            line = line.lower()
            words = line.split(" ")
            for word in words:
                if len(word) > 5:
                    frequency[word] = frequency.get(word, 0) + 1

    top_10 = list(frequency.items())
    top_10.sort(key=lambda x: x[1], reverse=True)
    top_words = [word for word, _ in top_10[:10]]
    return top_words

if __name__ == "__main__":
    print(top_10_words("williamson.txt"))