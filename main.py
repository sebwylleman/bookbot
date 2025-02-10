def get_character_count(text: str) -> dict[str, int]:
    character_count = {}
    lowercase_text = text.lower()

    for character in lowercase_text:
        if character not in character_count:
            character_count[character] = 0
        character_count[character] += 1

    return character_count


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_book_text() -> str:
    with open("books/frankenstein.txt") as f:
        return f.read()


def main():
    text = get_book_text()
    num_words = get_num_words(text)
    character_count = get_character_count(text)


main()
