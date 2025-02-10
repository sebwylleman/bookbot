def get_char_count(text: str) -> dict[str, int]:
    char_count = {}
    lowercase_text = text.lower()

    for char in lowercase_text:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    return char_count


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_book_text() -> str:
    with open("books/frankenstein.txt") as f:
        return f.read()


def convert_to_list_of_dicts(char_count: dict[str, int]) -> list[dict[str, int]]:
    result = []

    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        result.append(char_dict)

    return result


def sort_on(char_count):
    return char_count["count"]


def sort_char_count(list_of_char_count):
    return list_of_char_count.sort(reverse=True, key=sort_on)

def print_char_stat(sorted_chars):
    for char_count in sorted_chars:
        char = char_count["char"]
        if char.isalpha():
            count = char_count["count"]
            print(f"The '{char}' char was found {count} times")


def print_report(text: str, list_of_char_count: list[dict[str, int]]):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_num_words(text)} words found in the document")
    print_char_stat(list_of_char_count)
    print("--- End report ---")


def main():
    text = get_book_text()
    char_count = get_char_count(text)
    list_of_char_count = convert_to_list_of_dicts(char_count)
    sort_char_count(list_of_char_count)
    print_report(text, list_of_char_count)


main()
