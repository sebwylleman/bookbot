with open("books/frankenstein.txt") as file:
    file_contents = file.read()

    def count_words(file_contents):
        count = 0
        words = file_contents.split()
        return len(words)

    print(count_words(file_contents))
