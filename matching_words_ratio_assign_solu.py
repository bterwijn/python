import sys
import re

def main():
    if len(sys.argv) < 3:
        print_help()
        sys.exit(1)
    words1 = read_words(sys.argv[1])
    words2 = read_words(sys.argv[2])
    print(len(words1 & words2) / len(words1 | words2))
    
def read_words(filename):
    words = set()
    with open(filename) as file:
        for line in file:
            split = clean_up_text(line).split()
            for word in split:
                words.add(word)
    return words

def print_help():
    """ Prints usage information """
    print("usage: python", sys.argv[0], "<filename1> <filename2>")
    print("Prints the ratio of the count of all unique words 'filename1' and 'filename2' have in common",
          "with the count of all unique words in 'filename1' and 'filename2' in total.")

def clean_up_text(text):
    """ Returns 'text' after conversion to lower case and replacing all non-letters with a whitespace. """
    text = text.lower()  # to lower case
    text = re.sub(r'[^a-z]', ' ', text)  # replace other characters than a-z with ' '
    return text

main()
