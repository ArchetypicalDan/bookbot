from stats import *



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

    
def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_count = count_chars(book_text)
    char_report = report_counts(char_count)
    print_report(filepath, num_words, char_report)
    

main()