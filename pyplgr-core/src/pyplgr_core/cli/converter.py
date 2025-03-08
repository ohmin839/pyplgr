import sys

from ..api import to_polytonic

def main():
    for line in sys.stdin:
        print(to_polytonic(line), end='')

if __name__ == '__main__':
    main()
