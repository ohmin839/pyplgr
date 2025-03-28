# pyplgr-core
`pyplgr-core` provides some APIs and CLIs.

## API
- `to_polytonic` function converts ASCII strings into strings in polytonic Greek.
- `to_token_list` function splits texts in polytonic Greek into tokens.
```python
from pyplgr_core.api import to_polytonic, to_token_list

converted = to_polytonic("<o >'anthr^op'os tis")
print(converted) # ὁ ἄνθρωπός τις

split = to_token_list(converted)
print(split) # ['ὁ', 'ἄνθρωπός', 'τις']
```

## CLI

### pyplgrconv
`pyplgrconv` command converts ASCII strings into strings in polytonic Greek.
```bash
$ echo "<o >'anthr^op'os tis" | pyplgrconv
ὁ ἄνθρωπός τις
```

### pyplgrtknz
`pyplgrtknz` command extracts tokens uniquely from texts in polytonic Greek.
```bash
$ head -n1 alpha.txt | pyplgrconv | pyplgrtknz
Πάντες
ἄνθρωποι
τοῦ
εἰδέναι
ὀρέγονται
φύσει
.
σημεῖον
δ'
```
