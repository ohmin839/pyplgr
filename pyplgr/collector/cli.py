import sys
from .api import to_words_list

def main():
    for line in sys.stdin:
        words = to_words_list(line)
        for w in words:
            print(w)

if __name__ == '__main__':
    main()