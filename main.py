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


def sorted_dict(char_count):
    sorted_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_count


def main():
    path = "./books/frankenstein.txt"
    file_contents = get_book_text(path)
    total_num_words = count_words(file_contents)
    char_count = count_chars(file_contents)

    print(
        f"--- Begin report of books/frankenstein.txt ---\n{count_words(file_contents)} words found in the document"
    )
    print()
    print(sorted_dict(char_count))


main()
