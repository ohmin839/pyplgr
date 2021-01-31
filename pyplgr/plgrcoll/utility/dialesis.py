def without_dialesis(char):
    if char in 'ϊ': return 'ι'
    if char in 'ΐ': return 'ί'
    if char in 'ῒ': return 'ὶ'
    if char in 'ῗ': return 'ῖ'
    if char in 'ϋ': return 'υ'
    if char in 'ΰ': return 'ύ'
    if char in 'ῢ': return 'ὺ'
    if char in 'ῧ': return 'ῦ'
    return char
