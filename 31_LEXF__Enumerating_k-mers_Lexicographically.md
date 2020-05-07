# 31. Enumerating k-mers Lexicographically
```python
## Organizing Strings

# Date : 20.03.28 (Sat)

## 00. Import Library

from itertools import product


## 01. Set Variables

result_ls = []


## 02. Read File

with open("rosalind_lexf.txt") as f :
	fr = f.readlines()

	seq_ls = fr[0].replace("\n", "").split(" ")
	n = int(fr[1])


## 03. Get the Result

result = list(product(seq_ls, repeat = 3))

for x in result :
	for i in range(len(x)) :
		print(x[i], end = "")
	print("")
```
## Link
> [Enumerating k-mers Lexicographically](http://rosalind.info/problems/lexf/)
