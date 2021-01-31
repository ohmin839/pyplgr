def is_to_be_eliminated(char):
    if char == ',': return True
    if char == '·': return True
    if char == '.': return True
    if char == ';': return True
    if char == '«': return True
    if char == '»': return True
    if char == '-': return True
    if char == '(': return True
    if char == ')': return True
    if char == '<': return True
    if char == '>': return True
    if char == '[': return True
    if char == ']': return True
    return False

