from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book_text)} total words")

main()
