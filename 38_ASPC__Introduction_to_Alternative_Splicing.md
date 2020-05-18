# 38 Introduction to Alternative Splicing
```python
## The Baby and the Bathwater

# Date : 20.04.10 (Fri)

## 00. Import Library

import math


## 01. Define Function

def comb(n, r) :
	result = math.factorial(n) / (math.factorial(n - r) * math.factorial(r))
	result %= 1000000

	return result


## 02. Set Variables

result = 0


## 03. Read File

with open("rosalind_aspc.txt") as f :
	n, m = map(int, f.read().strip().split(" "))


## 03. Add the Number of Combination

for i in range(m, n + 1) :
	result += comb(n, i)

result %= 1000000

print(result)
```
## Link
> [Introduction to Alternative Splicing](http://rosalind.info/problems/aspc/)
