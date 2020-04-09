# 16. Enumerating Gene Orders
```python
## Rearrangements Power Large-Scale Genomic Changes

# Date : 20.03.09 (Mon)

## 00. Import Library

from itertools import permutations


## 01. Set Variables

num_ls = []
result = 1


## 02. Read File

with open("rosalind_perm.txt") as f :
	num = int(f.read().replace("\n", ""))


### 03. Create num_ls

for i in range(num) :
	num_ls.append(i + 1)


## 04. Calculate a Set of Permutations

for i in range(num) :
	result *= (i + 1)


## 05. Print the Result

com_ls = list(permutations(num_ls, num))

for i in range(result) :
	for j in range(len(com_ls[i])) :
		print(com_ls[i][j], end = " ") 
	print("")
```
## Link
> [Enumerating Gene Orders](http://rosalind.info/problems/perm/)
