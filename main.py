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

    def print_letter_count(file_contents):
        count_dict = count_letter(file_contents)
        for key in count_dict:
            print(f"The '{key}' character was found {count_dict[key]} times")

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print_letter_count(file_contents)
    print("--- End report ---")
