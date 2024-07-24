# pyplgrapi
`pyplgrapi` provides some APIs as functions.

## Conversion API
`to_polytonic` function converts an ASCII string into a string in polytonic Greek.
```python
from pyplgrapi import to_polytonic

converted = to_polytonic(">'anthr^opos")
print(converted) # ἄνθρωπος
```

## Collection API
`to_words_list` function splits a text in polytonic Greek into words:
```python
from pyplgrapi import to_words_list

converted = to_polytonic("<o >'anthr^op'os tis")
split = to_words_list(converted)
print(split) # ['ὁ', 'ἄνθρωπός', 'τις']
```

## Conversion Rules
(Under construction)