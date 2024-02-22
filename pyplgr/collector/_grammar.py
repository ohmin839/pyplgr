from parsimonious.grammar import Grammar

grammar = Grammar(
    r"""
    words = (word / any_char)*
    word = alphabet+ apostroph?

    alphabet
        = large_alpha
        / large_epsilon
        / large_eta
        / large_iota
        / large_omicron
        / large_upsilon
        / large_omega
        / large_rho
        / large_consonant
        / small_alpha
        / small_epsilon
        / small_eta
        / small_iota
        / small_omicron
        / small_upsilon
        / small_omega
        / small_rho
        / small_consonant

    large_alpha = ~r"[ΑἈἌᾌἊᾊἎᾎᾈἉἍᾍἋᾋᾋἏᾉΆᾺᾼ]"
    large_epsilon = ~r"[ΕἘἜἚἙἝἛΈῈ]"
    large_eta = ~r"[ΗἨἬᾜἪᾚἮᾞᾘἩἭᾝἫᾛᾛἯᾙΉῊῌ]"
    large_iota = ~r"[ΙἸἼἺἾἹἽἻἿΊῚΪ]"
    large_omicron = ~r"[ΟὈὌὊὉὍὋΌῸ]"
    large_upsilon = ~r"[ΥὙὝὛὟΎῪΫ]"
    large_omega = ~r"[ΩὨὬᾬὪᾪὮᾮᾨὩὭᾭὫᾫᾫὯᾩΏῺῼ]"
    large_rho = ~r"[ΡῬ]"
    large_consonant = ~r"[ΒΓΔΖΘΚΛΜΝΞΠΣΤΦΧΨ]"

    small_alpha = ~r"[αἀἄᾄἂᾂἆᾆᾀἁἅᾅἃᾃᾃἇᾁάᾴὰᾲᾶᾷᾳ]"
    small_epsilon = ~r"[εἐἔἒἑἕἓέὲ]"
    small_eta = ~r"[ηἠἤᾔἢᾒἦᾖᾐἡἥᾕἣᾓᾓἧᾑήῄὴῂῆῇῃ]"
    small_iota = ~r"[ιἰἴἲἶἱἵἳἷίὶῖϊΐῒῗ]"
    small_omicron = ~r"[οὀὄὂὁὅὃόὸ]"
    small_upsilon = ~r"[υὐὔὒὖὑὕὓὗύὺῦϋΰῢῧ]"
    small_omega = ~r"[ωὠὤᾤὢᾢὦᾦᾠὡὥᾥὣᾣᾣὧᾡώῴὼῲῶῷῳ]"
    small_rho = ~r"[ρῤῥ]"
    small_consonant = ~r"[βγδζθκλμνξπσςτφχψ]"

    apostroph = "'"

    any_char = ~r"\r?\n" / ~r"."
    """
)