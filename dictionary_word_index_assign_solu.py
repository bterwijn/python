import sys
import re

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
    word_index = index_words(sys.argv[1])
    print_word_index_alphabetically(word_index)

def print_help():
    """ Prints usage information """
    print("usage: python", sys.argv[0], "<filename>")
    print("Prints the index of 'filename' where each word has a list of all the line numbers it appears on.",
          "The words in the index are sorted alphabetically.")

def clean_up_text(text):
    """ Returns 'text' after convertion to lower case and replacing all non-letters with a whitespace. """
    text = text.lower()  # to lower case
    text = re.sub(r'[^a-z]', ' ', text)  # replace other characters than a-z with ' '
    return text

def index_words(filename):
    """ Returns a dictionary with a key for each word in 'filename' and as value a list of lines it appears on. """
    word_index = {}
    with open(filename) as file:
        line_number = 0
        for line in file:
            words = clean_up_text(line).split()
            for word in words:
                add_line_number(word_index, word, line_number)
            line_number += 1
    return word_index

def add_line_number(word_index, word, line_number):
    """ Adds 'line_number' to key 'word' in 'word_index' dictionary, where the value is a list
    of line numbers. Duplicate line numbers are discarded. """
    if word not in word_index:
        word_index[word] = [line_number]
    else:
        if word_index[word][-1] != line_number:
            word_index[word].append(line_number)

def print_word_index_alphabetically(word_index):
    """ Prints each key in 'word_index' in alphabetical order together with its value. """
    word_index_list = list(word_index.items())
    word_index_list.sort()
    for word, index in word_index_list:
        print(word, ":", index)

main()
