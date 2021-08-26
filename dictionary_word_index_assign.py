import sys
import re

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

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

main()
