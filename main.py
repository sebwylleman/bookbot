def get_book_text(path):
    with open(path) as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def main():
    path = "./books/frankenstein.txt"
    file_contents = get_book_text(path)
    total_num_words = count_words(file_contents)
    print(total_num_words)


main()
