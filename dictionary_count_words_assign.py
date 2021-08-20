import sys
import re

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

def print_help():
    """ Prints usage information """
    print("usage: python", sys.argv[0], "<filename>")
    print("Print the top 20 of most occuring words in 'filename' together with their count.",
          "The words are sorted by their count from high to low.")

def clean_up_text(text):
    """ Returns 'text' after conversion to lower case and replacing all non-letters with a whitespace. """
    text = text.lower()  # to lower case
    text = re.sub(r'[^a-z]', ' ', text)  # replace other characters than a-z with ' '
    return text

main()
