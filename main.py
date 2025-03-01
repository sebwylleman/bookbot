from stats import (
    convert_to_list_of_dicts,
    get_book_text,
    get_char_count,
    print_report,
    sort_char_count,
)


def main():
    text = get_book_text()
    char_count = get_char_count(text)
    list_of_char_count = convert_to_list_of_dicts(char_count)
    sort_char_count(list_of_char_count)
    print_report(text, list_of_char_count)


main()
