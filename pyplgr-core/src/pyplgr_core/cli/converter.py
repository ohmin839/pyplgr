import re, sys

from ..api import to_polytonic

def main():
    comment_pattern = re.compile(r'^%.*$')
    for line in sys.stdin:
        if not comment_pattern.match(line):
            print(to_polytonic(line), end='')

if __name__ == '__main__':
    main()
