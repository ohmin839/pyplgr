def create_polytonic_converter():
    def to_polytonic(text):
        from .lexer import create_lexer
        from .parser import create_parser

        lexer = create_lexer()
        parser = create_parser()

        return parser.parse(text, lexer=lexer)
    return to_polytonic

to_polytonic = create_polytonic_converter()

