import sys

from stats import (
    convert_to_list_of_dicts,
    get_book_text,
    get_char_count,
    print_report,
    sort_char_count,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    char_count = get_char_count(text)
    list_of_char_count = convert_to_list_of_dicts(char_count)
    sort_char_count(list_of_char_count)
    print_report(book_path, text, list_of_char_count)


main()
