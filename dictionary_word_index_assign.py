import sys
import re

def main():
    if len(sys.argv)<2:
        print_help()
        sys.exit(1)
    word_index=index_words(sys.argv[1])
    print_word_index_alphabetically(word_index)

def print_help():
    """ Prints usage information """
    print("usage: python", sys.argv[0], "<filename>")
    print("Prints the index of 'filename' where each word has a list of all the line numbers it appears in.",
          "The words are sorted alphabetically.")

def clean_up_text(text):
    """ Returns 'text' after convertion to lower case and replacing all non-letters with a whitespace. """
    text=text.lower() # to lower case             
    text=re.sub(r'[^a-z]',' ',text) # replace other characters than a-z with ' '
    return text

def index_words(filename):
    """ Returns a dictionary with a key for each word in 'filename' and as value a list of lines it appears on. """
    word_index={}
    with open(filename) as file:
        line_count=0
        for line in file:
            split=clean_up_text(line).split()
            for word in split:
                if word not in word_index:
                    word_index[word]=[]
                word_index[word].append(line_count)
            line_count+=1
    return word_index

def print_word_index_alphabetically(word_index):
    """ Prints each key in 'word_index' in alphabetical order together with its value. """
    word_index_list=list(word_index.items())
    word_index_list.sort()
    for word, index in word_index_list:
        print(word,":",index)

main()
