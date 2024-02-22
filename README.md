# pyplgr
**pyplgr** is a text processor for texts in polytonic Greek.\
**CAUTION: this is a work in progress.**

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
