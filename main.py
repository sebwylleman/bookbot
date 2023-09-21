def get_book_text(path):
    with open(path) as file:
        return file.read()


def count_words(words):
    return len(words)


def count_chars(words):
    count = {}
    for word in words:
        for char in word.lower():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


def reverse_sort_count(count):
    return sorted(count.items(), key=lambda item: item[1], reverse=True)


def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    words = text.split()
    total_num_words = count_words(words)
    count = count_chars(words)
    reverse_count = reverse_sort_count(count)

    print(
        f"--- Begin report of books/frankenstein.txt ---\n{total_num_words} words found in the document"
    )
    print()
    for item in reverse_count:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print()
    print("--- End report ---")


main()
