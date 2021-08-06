import sys

def main():
    print('Command line arguments:', sys.argv)
    print('Number of arguments:', len(sys.argv))
    print(type(sys.argv[0]))  # <class 'str'>

main()
