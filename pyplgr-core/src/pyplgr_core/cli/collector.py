import sys
from ordered_set import OrderedSet

from ..api import to_words_list

def main():
    words_set = OrderedSet() 
    for line in sys.stdin:
        words_list = to_words_list(line)
        for w in words_list:
            words_set.add(w)
    else:
        for w in words_set:
            print(w)

if __name__ == '__main__':
    main()
