# pyplgrcore
`pyplgrcore` provides some APIs and CLIs.

## API
- `to_polytonic` function converts ASCII strings into strings in polytonic Greek.
- `to_words_list` function splits texts in polytonic Greek into words.
```python
from pyplgrcore.api import to_polytonic, to_words_list

converted = to_polytonic("<o >'anthr^op'os tis")
print(converted) # ὁ ἄνθρωπός τις

split = to_words_list(converted)
print(split) # ['ὁ', 'ἄνθρωπός', 'τις']
```

## CLI

### pyplgrconv
`pyplgrconv` command converts ASCII strings into strings in polytonic Greek.
```bash
$ echo "<o >'anthr^op'os tis" | pyplgrconv
ὁ ἄνθρωπός τις
```

### pyplgrcoll
`pyplgrcoll` command extracts words uniquely from texts in polytonic Greek.
```bash
$ cat alpha.txt | pyplgrconv | pyplgrcoll
Πάντες
ἄνθρωποι
τοῦ
εἰδέναι
ὀρέγονται
φύσει
σημεῖον
δ'
...
```
