import sys
from .lexer import Lexer
from .api import to_lower

def collect_distinct_words():
    words = set()
    lexer = Lexer()
    lexer.build()
    for line in sys.stdin:
        lexer.lexer.input(line)
        while True:
             tok = lexer.lexer.token()
             if not tok:
                 break
             else:
                w = tok.value
                words.add(w)
    return words

def main():
    words = collect_distinct_words()
    for w in words:
        print(w)

if __name__ == '__main__':
    main()
