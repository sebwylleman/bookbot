with open("books/frankenstein.txt") as file:
    file_contents = file.read()

    def count_words(file_contents):
        count = 0
        words = file_contents.split()
        return len(words)

    def count_letter(file_contents):
        result = {}
        for letter in file_contents:
            char = letter.lower()
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
        return result

    print(count_letter(file_contents))
