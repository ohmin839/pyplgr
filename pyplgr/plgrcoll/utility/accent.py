def without_accent(char):
    # small alpha
    if char in 'άὰᾶ': return 'α'
    if char in 'ᾴᾲᾷ': return 'ᾳ'
    if char in 'ἅἃἇ': return 'ἁ'
    if char in 'ᾅᾃᾇ': return 'ᾁ'
    if char in 'ἄἂἆ': return 'ἀ'
    if char in 'ᾄᾂᾆ': return 'ᾀ'
    # small epsilon
    if char in 'έὲ': return 'ε'
    if char in 'ἕἓ': return 'ἑ'
    if char in 'ἔἒ': return 'ἐ'
    # small eta
    if char in 'ήὴῆ': return 'η'
    if char in 'ῄῂῇ': return 'ῃ'
    if char in 'ἥἣἧ': return 'ἡ'
    if char in 'ᾕᾓᾗ': return 'ᾑ'
    if char in 'ἤἢἦ': return 'ἠ'
    if char in 'ᾔᾒᾖ': return 'ᾐ'
    # small iota
    if char in 'ίὶῖ': return 'ι'
    if char in 'ἵἳἷ': return 'ἱ'
    if char in 'ἴἲἶ': return 'ἰ'
    if char in 'ΐῒῗ': return 'ϊ'
    # small omicron
    if char in 'όὸ': return 'ο'
    if char in 'ὅὃ': return 'ὁ'
    if char in 'ὄὂ': return 'ὀ'
    # small upsilon
    if char in 'ύὺῦ': return 'υ'
    if char in 'ὕὓὗ': return 'ὑ'
    if char in 'ὔὒὖ': return 'ὐ'
    if char in 'ΰῢῧ': return 'ϋ'
    # small omega
    if char in 'ώὼῶ': return 'ω'
    if char in 'ῴῲῷ': return 'ῳ'
    if char in 'ὥὣὧ': return 'ὡ'
    if char in 'ᾥᾣᾧ': return 'ᾡ'
    if char in 'ὤὢὦ': return 'ὠ'
    if char in 'ᾤᾢᾦ': return 'ᾠ'
    # large alpha
    if char in 'ΆᾺ': return 'Α'
    if char in 'ἍἋἏ': return 'Ἁ'
    if char in 'ᾍᾋᾏ': return 'ᾉ'
    if char in 'ἌἊἎ': return 'Ἀ'
    if char in 'ᾌᾊᾎ': return 'ᾈ'
    # large epsilon
    if char in 'ΈῈ': return 'Ε'
    if char in 'ἝἛ': return 'Ἑ'
    if char in 'ἜἚ': return 'Ἐ'
    # large eta
    if char in 'ΉῊ': return 'Η'
    if char in 'ἭἫἯ': return 'Ἡ'
    if char in 'ᾝᾛᾟ': return 'ᾙ'
    if char in 'ἬἪἮ': return 'Ἠ'
    if char in 'ᾜᾚᾞ': return 'ᾘ'
    # large iota
    if char in 'ΊῚ': return 'Ι'
    if char in 'ἽἻἿ': return 'Ἱ'
    if char in 'ἼἺἾ': return 'Ἰ'
    # large omicron
    if char in 'ΌῸ': return 'Ο'
    if char in 'ὍὋ': return 'Ὁ'
    if char in 'ὌὊ': return 'Ὀ'
    # large upsilon
    if char in 'ΎῪ': return 'Υ'
    if char in 'ὝὛὟ': return 'Ὑ'
    # large omega
    if char in 'ΏῺ': return 'Ω'
    if char in 'ὭὫὯ': return 'Ὡ'
    if char in 'ᾭᾫᾯ': return 'ᾩ'
    if char in 'ὬὪὮ': return 'Ὠ'
    if char in 'ᾬᾪᾮ': return 'ᾨ'
    return char

