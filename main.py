with open("books/frankenstein.txt") as file:
    file_contents = file.read()

    def count_words(file_contents):
        count = 0
        words = file_contents.split()
        return len(words)

    def count_letter(file_contents):
        result = {}
        for char in file_contents:
            if char.isalpha():
                letter = char.lower()
                if letter in result:
                    result[letter] += 1
                else:
                    result[letter] = 1
        return result

    print(count_letter(file_contents))
