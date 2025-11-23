from stats import get_num_words, count_letters, pretty_sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    letter_dict = count_letters(book_text)
    print(f"Found {get_num_words(book_text)} total words")
    pretty_sort(letter_dict)

main()
