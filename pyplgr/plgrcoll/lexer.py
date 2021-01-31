import ply.lex as lex
from ply.lex import TOKEN

class Lexer:
    tokens = (
        "WORD",    
        "APOSTROPH",
        "NEWLINE",
        "OTHERS",
    )

    large_alpha = "[ΑἈἌᾌἊᾊἎᾎᾈἉἍᾍἋᾋᾋἏᾉΆᾺᾼ]"
    large_epsilon = "[ΕἘἜἚἙἝἛΈῈ]"
    large_eta = "[ΗἨἬᾜἪᾚἮᾞᾘἩἭᾝἫᾛᾛἯᾙΉῊῌ]"
    large_iota = "[ΙἸἼἺἾἹἽἻἿΊῚΪ]"
    large_omicron = "[ΟὈὌὊὉὍὋΌῸ]"
    large_upsilon = "[ΥὙὝὛὟΎῪΫ]"
    large_omega = "[ΩὨὬᾬὪᾪὮᾮᾨὩὭᾭὫᾫᾫὯᾩΏῺῼ]"
    large_rho = "[ΡῬ]"
    large_consonant = "[ΒΓΔΖΘΚΛΜΝΞΠΣΤΦΧΨ]"

    small_alpha = "[αἀἄᾄἂᾂἆᾆᾀἁἅᾅἃᾃᾃἇᾁάᾴὰᾲᾶᾷᾳ]"
    small_epsilon = "[εἐἔἒἑἕἓέὲ]"
    small_eta = "[ηἠἤᾔἢᾒἦᾖᾐἡἥᾕἣᾓᾓἧᾑήῄὴῂῆῇῃ]"
    small_iota = "[ιἰἴἲἶἱἵἳἷίὶῖϊΐῒῗ]"
    small_omicron = "[οὀὄὂὁὅὃόὸ]"
    small_upsilon = "[υὐὔὒὖὑὕὓὗύὺῦϋΰῢῧ]"
    small_omega = "[ωὠὤᾤὢᾢὦᾦᾠὡὥᾥὣᾣᾣὧᾡώῴὼῲῶῷῳ]"
    small_rho = "[ρῤῥ]"
    small_consonant = "[βγδζθκλμνξπσςτφχψ]"

    alphabet = "(" + large_alpha + \
                "|" + large_epsilon + \
                "|" + large_eta + \
                "|" + large_iota + \
                "|" + large_omicron + \
                "|" + large_upsilon + \
                "|" + large_omega + \
                "|" + large_rho + \
                "|" + large_consonant + \
                "|" + small_alpha + \
                "|" + small_epsilon + \
                "|" + small_eta + \
                "|" + small_iota + \
                "|" + small_omicron + \
                "|" + small_upsilon + \
                "|" + small_omega + \
                "|" + small_rho + \
                "|" + small_consonant + ")"

    apostroph = "'"

    word = alphabet + "+" \
            + "(" + apostroph + alphabet + "*" + ")?"

    @TOKEN(word)
    def t_WORD(self, t):
        return t

    def t_NEWLINE(self, t):
        "\\r?\\n"
        pass
    
    def t_OTHERS(self, t):
        "."
        pass
    
    def t_error(self, t):
        pass
    
    def __init__(self):
        self.lexer = None
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)

if __name__ == "__main__":
    import sys
    lexer = Lexer()
    lexer.build()
    lexer.test(sys.argv[1])

