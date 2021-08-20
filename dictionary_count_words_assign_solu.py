import sys
import re

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
    word_counts = count_words(sys.argv[1])
    print_top_n_words(word_counts, 20)

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

def count_words(filename):
    """ Returns a dictionary with a key for each word in 'filename' and as value the count of the word. """
    word_counts = {}
    with open(filename) as file:
        for line in file:
            split = clean_up_text(line).split()
            for word in split:
                if word not in word_counts:
                    word_counts[word] = 0
                word_counts[word] += 1
    return word_counts

def print_top_n_words(word_counts, n):
    """ Prints the sorted top 'n' of the most common words in 'word_counts' """
    word_counts_list = list(word_counts.items())
    word_counts_list.sort(key=lambda e: e[1], reverse=True)
    for word, count in word_counts_list[:n]:
        print(word, ":", count)

main()
