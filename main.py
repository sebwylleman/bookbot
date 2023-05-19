with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    def count_words(file_contents):
        count = 0
        words = file_contents.split()
        for word in words:
            count += 1
        return count

    print(count_words(file_contents))
