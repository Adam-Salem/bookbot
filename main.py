from stats import word_count
from stats import letter_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "books/frankenstein.txt"
    book_output = get_book_text(filepath)
    total_words = word_count(book_output)
    total_letters = letter_count(book_output)
    print(f"{total_words} words found in the document")
    print(total_letters)

main()