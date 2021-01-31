# pyplgr
**pyplgr** is a text processor for texts in polytonic Greek.\
**CAUTION: this is a work in progress.**

## Requirements
pyplgr depends on [PLY](https://github.com/dabeaz/ply),
which is 100% python implementation of the lex and yacc tools.
PLY requires the use of Python 3.6 or greator, so does pyplgr.

## Examples
### pyplgrconv
```
$ echo ">anthr^opos" | pyplgrconv
ἄνθρωπος
```

### pyplgrcoll
```
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
