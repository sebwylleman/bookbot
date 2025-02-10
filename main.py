def get_character_count(words: list[str]) -> dict[str, int]:
    character_count = {}

    for word in words:
        for char in word.lower():
            if char not in character_count:
                character_count[char] = 0
            character_count[char] += 1

    return character_count


def get_num_words(words: list[str]) -> int:
    return len(words)


def get_book_text() -> str:
    with open("books/frankenstein.txt") as f:
        return f.read()


def main():
    file_contents = get_book_text()

    words = file_contents.split()
    get_num_words(words)
    print(get_character_count(words))


main()
