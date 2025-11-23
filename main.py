from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    letter_dict = count_letters(book_text)
    sorted_dict = pretty_sort(letter_dict)
    pretty_print(path, word_count, sorted_dict)
main()
