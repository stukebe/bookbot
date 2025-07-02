import sys
from stats import get_num_words, get_character_count, sort_dictionary


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    number_words = get_num_words(get_book_text(book_path))
    print(f"Found {number_words} total words")
    character_dic = get_character_count(get_book_text(book_path))
    print("--------- Character Count -------")
    sorted_list = sort_dictionary(character_dic)
    for pair in sorted_list:
        if pair["char"].isalpha():
            print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")


main()