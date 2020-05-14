# 27 Counting Subsets
```python
## Characters and SNPs

# Date : 20.04.06 (Mon)

## 00. Set Variables

result = 1


## 01. Read File

with open("rosalind_sset.txt") as f :
	num = int(f.readline().strip())


## 02. Count the Number of Possible Subsets

for i in range(num) :

	result = 2 ** num

	if result > 1000000 :
		result = result % 1000000

print(result)
```
## Link
> [Counting Subsets](http://rosalind.info/problems/sset/)
