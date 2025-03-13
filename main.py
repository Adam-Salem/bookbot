from stats import word_count
from stats import letter_count
from stats import dict_sort
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_output = get_book_text(filepath)
    total_words = word_count(book_output)
    total_letters = letter_count(book_output)
    sorted_letters = dict_sort(total_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_letters)):
        print(f"{sorted_letters[i]}: {total_letters[sorted_letters[i]]}")
    print("============= END ===============")

main()