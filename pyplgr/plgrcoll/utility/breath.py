def without_breath(char):
    # small alpha
    if char in 'ἁἀ': return 'α'
    if char in 'ᾁᾀ': return 'ᾳ'
    if char in 'ἅἄ': return 'ά'
    if char in 'ᾅᾄ': return 'ᾴ'
    if char in 'ἃἂ': return 'ὰ'
    if char in 'ᾃᾂ': return 'ᾲ'
    if char in 'ἇἆ': return 'ᾶ'
    if char in 'ᾇᾆ': return 'ᾷ'
    # small epsilon
    if char in 'ἑἐ': return 'ε'
    if char in 'ἕἔ': return 'έ'
    if char in 'ἓἒ': return 'ὲ'
    # small eta
    if char in 'ἡἠ': return 'η'
    if char in 'ᾑᾐ': return 'ῃ'
    if char in 'ἥἤ': return 'ή'
    if char in 'ᾕᾔ': return 'ῄ'
    if char in 'ἣἢ': return 'ὴ'
    if char in 'ᾓᾒ': return 'ῂ'
    if char in 'ἧἦ': return 'ῆ'
    if char in 'ᾗᾖ': return 'ῇ'
    # small iota
    if char in 'ἱἰ': return 'ι'
    if char in 'ἵἴ': return 'ί'
    if char in 'ἳἲ': return 'ὶ'
    if char in 'ἷἶ': return 'ῖ'
    # small omicron
    if char in 'ὁὀ': return 'ο'
    if char in 'ὅὄ': return 'ό'
    if char in 'ὃὂ': return 'ὸ'
    # small rho
    if char in 'ῥῤ': return 'ρ'
    # small upsilon
    if char in 'ὑὐ': return 'υ'
    if char in 'ὕὔ': return 'ύ'
    if char in 'ὓὒ': return 'ὺ'
    if char in 'ὗὖ': return 'ῦ'
    # small omega
    if char in 'ὡὠ': return 'ω'
    if char in 'ᾡᾠ': return 'ῳ'
    if char in 'ὥὤ': return 'ώ'
    if char in 'ᾥᾤ': return 'ῴ'
    if char in 'ὣὢ': return 'ὼ'
    if char in 'ᾣᾢ': return 'ῲ'
    if char in 'ὧὦ': return 'ῶ'
    if char in 'ᾧᾦ': return 'ῷ'
    # large alpha
    if char in 'ἉἈ': return 'Α'
    if char in 'ᾉᾈ': return 'ᾼ'
    if char in 'ἍἌ': return 'Ά'
    if char in 'ᾍᾌ': return 'ᾼ'
    if char in 'ἋἊ': return 'Ὰ'
    if char in 'ᾋᾊ': return 'ᾼ'
    if char in 'ἏἎ': return 'Α'
    if char in 'ᾏᾎ': return 'ᾼ'
    # large epsilon
    if char in 'ἙἘ': return 'Ε'
    if char in 'ἝἜ': return 'Έ'
    if char in 'ἛἚ': return 'Ὲ'
    # large eta
    if char in 'ἩἨ': return 'Η'
    if char in 'ᾙᾘ': return 'ῌ'
    if char in 'ἭἬ': return 'Ή'
    if char in 'ᾝᾜ': return 'ῌ'
    if char in 'ἫἪ': return 'Ὴ'
    if char in 'ᾛᾚ': return 'ῌ'
    if char in 'ἯἮ': return 'Η'
    if char in 'ᾟᾞ': return 'ῌ'
    # large iota
    if char in 'ἹἸ': return 'Ι'
    if char in 'ἽἼ': return 'Ί'
    if char in 'ἻἺ': return 'Ὶ'
    if char in 'ἿἾ': return 'Ι'
    # large omicron
    if char in 'ὉὈ': return 'Ο'
    if char in 'ὍὌ': return 'Ό'
    if char in 'ὋὊ': return 'Ὸ'
    # large rho
    if char in 'Ῥ': return 'Ρ'
    # large upsilon
    if char in 'Ὑ': return 'Υ'
    if char in 'Ὕ': return 'Ύ'
    if char in 'Ὓ': return 'Ὺ'
    if char in 'Ὗ': return 'Υ'
    # large omega
    if char in 'ὩὨ': return 'Ω'
    if char in 'ᾩᾨ': return 'ῼ'
    if char in 'ὭὬ': return 'Ώ'
    if char in 'ᾭᾬ': return 'ῼ'
    if char in 'ὫὪ': return 'Ὼ'
    if char in 'ᾫᾪ': return 'ῼ'
    if char in 'ὯὮ': return 'Ω'
    if char in 'ᾯᾮ': return 'ῼ'
    return char

