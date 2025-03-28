import sys

from ..api import to_token_list

def main():
    token_set = set()
    for line in sys.stdin:
        token_list = to_token_list(line)
        for t in token_list:
            if not t in token_set: 
                token_set.add(t)
                print(t)

if __name__ == '__main__':
    main()
