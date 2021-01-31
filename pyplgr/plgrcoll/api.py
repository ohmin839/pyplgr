from .utility.lower import to_lower as inner_to_lower
from .utility.upper import to_upper as inner_to_upper
from .utility.accent import without_accent as inner_without_accent
from .utility.breath import without_breath as inner_without_breath
from .utility.dialesis import without_dialesis as inner_without_dialesis
from .utility.iota import without_iota_subscriptum as inner_without_iota_subscriptum
from .utility.punctuation import is_to_be_eliminated

def to_lower(text):
    return ''.join([inner_to_lower(char) for char in text])

def to_upper(text):
    return ''.join([inner_to_upper(char) for char in text])

def without_accent(text):
    return ''.join([inner_without_accent(char) for char in text])

def without_breath(text):
    return ''.join([inner_without_breath(char) for char in text])

def without_dialesis(text):
    return ''.join([inner_without_dialesis(char) for char in text])

def without_iota_subscriptum(text):
    return ''.join([inner_without_iota_subscriptum(char) for char in text])

def to_sortable(text):
    return without_accent(
            without_breath(
                without_dialesis(
                    without_iota_subscriptum(
                        to_lower(text)))))

