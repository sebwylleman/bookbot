def get_book_text(path):
    with open(path) as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    char_count = {}
    words = text.split()
    for char in words:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count


def report(text):
    return f"--- Begin report of books/frankenstein.txt ---\n{count_words(text)} words found in the document"


def main():
    path = "./books/frankenstein.txt"
    file_contents = get_book_text(path)
    total_num_words = count_words(file_contents)
    print(report(file_contents))


main()
