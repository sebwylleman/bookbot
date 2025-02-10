def count_words(file_contents: str) -> int:
    words = file_contents.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))


main()
