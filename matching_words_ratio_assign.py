import sys
import re

def main():
    if len(sys.argv) < 3:
        print_help()
        sys.exit(1)

def print_help():
    """ Prints usage information """
    print("usage: python", sys.argv[0], "<filename1> <filename2>")
    print("Prints the ratio of the count of all unique words 'filename1' and 'filename2' have in common",
          "with the count of all unique words in 'filename1' and 'filename2' in total.")

def clean_up_text(text):
    """ Returns 'text' after convertion to lower case and replacing all non-letters with a whitespace. """
    text = text.lower()  # to lower case
    text = re.sub(r'[^a-z]', ' ', text)  # replace other characters than a-z with ' '
    return text

main()
