# 29. Partial Permutations
```python
## Partial Gene Orderings

# Date : 20.03.26 (Thu)

## 00. Set Variables
result = 1

## 01. Read File
with open("rosalind_pper.txt") as f :
	fr = f.readline()
	fr = fr.replace("\n", "")

	n = int(fr.split(" ")[0])
	k = int(fr.split(" ")[1])
	

## 02. Permutations
for i in range(k) :
	result *= n
	result %= 1000000
	n -= 1

print(result)
```
## Link
> [Partial Permutations](http://rosalind.info/problems/pper/)
