# 27. Independent Alleles
```python
## Mendel's Second Law

# Date : 20.03.24 (Tue)

## 00. Import Library

from functools import reduce
import operator as op


## 01. Define Function

def countComb(n, r) :
	r = min(r, n - r) 

	x = reduce(op.mul, range(n, n - r, -1) , 1)
	y = reduce(op.mul, range(1, r + 1), 1)

	answer = x / y
	return answer


## 02. Set Variables

result = 0


## 03. Read File

with open("rosalind_lia.txt") as f :
	k, n = map(int, f.read().strip().split(" "))


## 03. Process

total = 2 ** k

for i in range(n, total + 1) :
	tmp = 1

	for j in range(i) :
		tmp *= 1/4
	
	for j in range(total - i) :
		tmp *= 3/4

	tmp *= countComb(total, i)

	result += tmp


## 04. Print Result

result = round(result, 3)
print(result)
```
## Link
> [Independent Alleles](http://rosalind.info/problems/lia/)
