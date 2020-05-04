# 29. Partial Permutations
```python
## Partial Gene Orderings

# Date : 20.03.26 (Thu)

## 00. Set Variables

result = 1


## 01. Read File

with open("rosalind_pper.txt") as f :
	n, k = map(int, f.read().strip().split(" "))
	

## 02. Permutations
for i in range(k) :
	result *= n
	result %= 1000000
	n -= 1

print(result)
```
## Link
> [Partial Permutations](http://rosalind.info/problems/pper/)
