import sys
from stats import (
    get_num_words,
    get_num_letters,
    sort_letter_counts,
)


def main():
    #import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    
    print ("============ BOOKBOT ============") 
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    #from stats import get_num_words
    total = get_num_words(bookpath)
    #total = count_words(file_contents)
    print ( f"Found {total} total words")
    print ("--------- Character Count -------")
    #from stats import get_num_letters
    tally_dict = get_num_letters(bookpath)
    #from stats import sort_letter_counts
    sorted_list = sort_letter_counts(tally_dict)
    for char_dict in sorted_list:
        char = char_dict["letter"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print ("============= END ===============") 
    

main()