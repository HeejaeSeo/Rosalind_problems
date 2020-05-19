# 39. Matching Random Motifs
```python
## More Random Strings

# Date : 20.04.14 (Tue)

## 00. Set Variables

tmp = 1
seq_dic = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}


## 01. Read File

with open("rosalind_rstr.txt") as f :
	fr = f.read().split()

n = int(fr[0])
x = float(fr[1])
seq = fr[2]


## 02. Get Data

gc = x / 2
at = (1 - x) / 2

for x in seq :
	seq_dic[x] += 1


## 03. Calculate the Probability

tmp = at ** (seq_dic['A'] + seq_dic['T']) * gc ** (seq_dic['G'] + seq_dic['C'])
result = round(1 - ((1 - tmp) ** n), 3)

print(result)
```
## Link
> [Matching Random Motifs](http://rosalind.info/problems/rstr/)
