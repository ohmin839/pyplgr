import ply.lex as lex

from .mapping import convert_to_large_alpha
from .mapping import convert_to_large_epsilon
from .mapping import convert_to_large_eta
from .mapping import convert_to_large_iota
from .mapping import convert_to_large_omicron
from .mapping import convert_to_large_upsilon
from .mapping import convert_to_large_omega

from .mapping import convert_to_large_kappa
from .mapping import convert_to_large_pi
from .mapping import convert_to_large_rho
from .mapping import convert_to_large_tau

from .mapping import convert_to_small_alpha
from .mapping import convert_to_small_epsilon
from .mapping import convert_to_small_eta
from .mapping import convert_to_small_iota
from .mapping import convert_to_small_omicron
from .mapping import convert_to_small_rho
from .mapping import convert_to_small_upsilon
from .mapping import convert_to_small_omega

from .mapping import convert_to_small_kappa
from .mapping import convert_to_small_pi
from .mapping import convert_to_small_rho
from .mapping import convert_to_small_sigma
from .mapping import convert_to_small_tau

tokens = (
    "LARGE_ALPHA",
    "LARGE_EPSILON",
    "LARGE_ETA",
    "LARGE_IOTA",
    "LARGE_OMICRON",
    "LARGE_UPSILON",
    "LARGE_OMEGA",

    "LARGE_BETA",
    "LARGE_GAMMA",
    "LARGE_DELTA",
    "LARGE_ZETA",
    "LARGE_KAPPA",
    "LARGE_LAMBDA",
    "LARGE_MU",
    "LARGE_NU",
    "LARGE_XI",
    "LARGE_PI",
    "LARGE_RHO",
    "LARGE_SIGMA",
    "LARGE_TAU",

    "SMALL_ALPHA",
    "SMALL_EPSILON",
    "SMALL_ETA",
    "SMALL_IOTA",
    "SMALL_OMICRON",
    "SMALL_UPSILON",
    "SMALL_OMEGA",

    "SMALL_BETA",
    "SMALL_GAMMA",
    "SMALL_DELTA",
    "SMALL_ZETA",
    "SMALL_KAPPA",
    "SMALL_LAMBDA",
    "SMALL_MU",
    "SMALL_NU",
    "SMALL_XI",
    "SMALL_PI",
    "SMALL_RHO",
    "SMALL_SIGMA",
    "SMALL_TAU",

    "COMMA",
    "SEMICORON",
    "PERIOD",
    "QUESTION",
    "APOSTROPH",
    "LGUILLEMET",
    "RGUILLEMET",
    "EMDASH",

    "NEWLINE",
    "OTHERS",
)

def create_lexer():
    def t_LARGE_ALPHA(t):
        "[<>]?['`~]?A\\|?"
        t.value = convert_to_large_alpha(t.value)
        return t

    def t_LARGE_EPSILON(t):
        "[<>]?['`]?E"
        t.value = convert_to_large_epsilon(t.value)
        return t

    def t_LARGE_ETA(t):
        "[<>]?['`~]?\\^E\\|?"
        t.value = convert_to_large_eta(t.value)
        return t

    def t_LARGE_IOTA(t):
        "[<>\"]?['`~]?I"
        t.value = convert_to_large_iota(t.value)
        return t

    def t_LARGE_OMICRON(t):
        "[<>]?['`]?O"
        t.value = convert_to_large_omicron(t.value)
        return t

    def t_LARGE_UPSILON(t):
        "[<>\"]?['`~]?[UY]"
        t.value = convert_to_large_upsilon(t.value)
        return t

    def t_LARGE_OMEGA(t):
        "[<>]?['`~]?\\^O\\|?"
        t.value = convert_to_large_omega(t.value)
        return t


    def t_LARGE_BETA(t):
        "B"
        t.value = "\u0392"
        return t

    def t_LARGE_GAMMA(t):
        "G"
        t.value = "\u0393"
        return t

    def t_LARGE_DELTA(t):
        "D"
        t.value = "\u0394"
        return t

    def t_LARGE_ZETA(t):
        "Z"
        t.value = "\u0396"
        return t

    def t_LARGE_KAPPA(t):
        "Kh?"
        t.value = convert_to_large_kappa(t.value)
        return t

    def t_LARGE_LAMBDA(t):
        "L"
        t.value = "\u039B"
        return t

    def t_LARGE_MU(t):
        "M"
        t.value = "\u039C"
        return t

    def t_LARGE_NU(t):
        "N"
        t.value = "\u039D"
        return t

    def t_LARGE_XI(t):
        "X"
        t.value = "\u039E"
        return t

    def t_LARGE_PI(t):
        "P[hs]?"
        t.value = convert_to_large_pi(t.value)
        return t

    def t_LARGE_RHO(t):
        "<?R"
        t.value = convert_to_large_rho(t.value)
        return t

    def t_LARGE_SIGMA(t):
        "S"
        t.value = "\u03A3"
        return t

    def t_LARGE_TAU(t):
        "Th?"
        t.value = convert_to_large_tau(t.value)
        return t


    def t_SMALL_ALPHA(t):
        "[<>]?['`~]?a\\|?"
        t.value = convert_to_small_alpha(t.value)
        return t

    def t_SMALL_EPSILON(t):
        "[<>]?['`]?e"
        t.value = convert_to_small_epsilon(t.value)
        return t

    def t_SMALL_ETA(t):
        "[<>]?['`~]?\\^e\\|?"
        t.value = convert_to_small_eta(t.value)
        return t

    def t_SMALL_IOTA(t):
        "[<>\"]?['`~]?i"
        t.value = convert_to_small_iota(t.value)
        return t

    def t_SMALL_OMICRON(t):
        "[<>]?['`]?o"
        t.value = convert_to_small_omicron(t.value)
        return t

    def t_SMALL_UPSILON(t):
        "[<>\"]?['`~]?[uy]"
        t.value = convert_to_small_upsilon(t.value)
        return t

    def t_SMALL_OMEGA(t):
        "[<>]?['`~]?\\^o\\|?"
        t.value = convert_to_small_omega(t.value)
        return t


    def t_SMALL_BETA(t):
        "b"
        t.value = "\u03B2"
        return t

    def t_SMALL_GAMMA(t):
        "g"
        t.value = "\u03B3"
        return t

    def t_SMALL_DELTA(t):
        "d"
        t.value = "\u03B4"
        return t

    def t_SMALL_ZETA(t):
        "z"
        t.value = "\u03B6"
        return t

    def t_SMALL_KAPPA(t):
        "kh?"
        t.value = convert_to_small_kappa(t.value)
        return t

    def t_SMALL_LAMBDA(t):
        "l"
        t.value = "\u03BB"
        return t

    def t_SMALL_MU(t):
        "m"
        t.value = "\u03BC"
        return t

    def t_SMALL_NU(t):
        "n"
        t.value = "\u03BD"
        return t

    def t_SMALL_XI(t):
        "x"
        t.value = "\u03BE"
        return t

    def t_SMALL_PI(t):
        "p[hs]?"
        t.value = convert_to_small_pi(t.value)
        return t

    def t_SMALL_RHO(t):
        "[<>]?r"
        t.value = convert_to_small_rho(t.value)
        return t

    def t_SMALL_SIGMA(t):
        "[sc]"
        t.value = convert_to_small_sigma(t.value)
        return t

    def t_SMALL_TAU(t):
        "th?"
        t.value = convert_to_small_tau(t.value)
        return t


    def t_COMMA(t):
        ","
        return t

    def t_SEMICORON(t):
        ";"
        t.value = "\u0387"
        return t

    def t_PERIOD(t):
        "\\."
        return t

    def t_QUESTION(t):
        "\\?"
        t.value = "\u037E"
        return t

    def t_APOSTROPH(t):
        "''"
        t.value = "'"
        return t

    def t_LGUILLEMET(t):
        "<<"
        t.value = "\u00AB"
        return t

    def t_RGUILLEMET(t):
        ">>"
        t.value = "\u00BB"
        return t

    def t_EMDASH(t):
        "--"
        t.value = "\u2014"
        return t


    def t_NEWLINE(t):
        "\\r?\\n"
        return t

    def t_OTHERS(t):
        "."
        return t


    def t_error(t):
        pass

    return lex.lex()

if __name__ == "__main__":
    import sys
    lexer = create_lexer()
    lexer.input(sys.argv[1])
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
