from stats import count_words,count_chars,get_sorted_list
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_report(path):
    text = get_book_text(path)
    char_dict = get_sorted_list(count_chars(text))

    print(f"Found {count_words(text)} total words")
    for char in char_dict:
        print(f"{char[0]}: {char[1]} \n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print_report(path)
    

main()