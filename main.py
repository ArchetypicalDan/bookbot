import sys
from stats import *
from pathlib import Path


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(filepath, num_words, char_report):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_report:
        if(item["char"].isalpha()):
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

    
def main(argv):
    if len(argv) < 2 or len(argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = Path(argv[1])

    if not filepath.is_file():
        print(f"Error: Could not find file \'{filepath}\'")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_count = count_chars(book_text)
    char_report = report_counts(char_count)
    print_report(filepath, num_words, char_report)
    

main(sys.argv)