with open("./books/frankenstein.txt") as file:
    file_contents = file.read()

    def count_words(text):
        words = text.split()
        return len(words)

    print(count_words(file_contents))
