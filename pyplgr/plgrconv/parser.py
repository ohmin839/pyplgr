import ply.yacc as yacc

def create_parser():
    from .lexer import tokens

    def p_letters(p):
        """letters  :
                    | letter
                    | letter letters"""
        if len(p) > 1:
            p[0] = "".join(p[1:])
        else:
            p[0] = ""

    def p_letter(p):
        """letter   : alphabet 
                    | punctuation
                    | NEWLINE
                    | OTHERS"""
        p[0] = p[1]

    def p_alphabet(p):
        """alphabet : non_final_sigma
                    | large_nasable_gamma
                    | small_nasable_gamma
                    | single_alphabet"""
        p[0] = p[1]

    def p_non_final_sigma(p):
        """non_final_sigma : SMALL_SIGMA alphabet"""
        p[0] = "\u03C3" + p[2]

    def p_large_nasable_gamma(p):
        """large_nasable_gamma  : LARGE_NU LARGE_GAMMA
                                | LARGE_NU LARGE_KAPPA
                                | LARGE_NU LARGE_XI"""
        p[0] = "\u0393" + p[2]

    def p_small_nasable_gamma(p):
        """small_nasable_gamma  : SMALL_NU SMALL_GAMMA
                                | SMALL_NU SMALL_KAPPA
                                | SMALL_NU SMALL_XI"""
        p[0] = "\u03B3" + p[2]

    def p_single_alphabet(p):
        """single_alphabet      : LARGE_ALPHA
                                | LARGE_BETA 
                                | LARGE_GAMMA
                                | LARGE_DELTA
                                | LARGE_EPSILON
                                | LARGE_ZETA
                                | LARGE_ETA
                                | LARGE_IOTA
                                | LARGE_KAPPA
                                | LARGE_LAMBDA
                                | LARGE_MU
                                | LARGE_NU
                                | LARGE_XI
                                | LARGE_OMICRON
                                | LARGE_PI
                                | LARGE_RHO
                                | LARGE_SIGMA
                                | LARGE_TAU
                                | LARGE_UPSILON
                                | LARGE_OMEGA
                                | SMALL_ALPHA
                                | SMALL_BETA 
                                | SMALL_GAMMA
                                | SMALL_DELTA
                                | SMALL_EPSILON
                                | SMALL_ZETA
                                | SMALL_ETA
                                | SMALL_IOTA
                                | SMALL_KAPPA
                                | SMALL_LAMBDA
                                | SMALL_MU
                                | SMALL_NU
                                | SMALL_XI
                                | SMALL_OMICRON
                                | SMALL_PI
                                | SMALL_RHO
                                | SMALL_SIGMA
                                | SMALL_TAU
                                | SMALL_UPSILON
                                | SMALL_OMEGA"""
        p[0] = p[1]

    def p_punctuation(p):
        """punctuation      : COMMA
                            | SEMICORON
                            | PERIOD
                            | QUESTION
                            | APOSTROPH
                            | LGUILLEMET
                            | RGUILLEMET
                            | EMDASH"""
        p[0] = p[1]


    def p_error(p):
        pass

    return yacc.yacc(debug=False)

if __name__ == "__main__":
    import sys
    from .lexer import create_lexer
    lexer = create_lexer()
    parser = create_parser()
    print(parser.parse(sys.argv[1], lexer=lexer))

