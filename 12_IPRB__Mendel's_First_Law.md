# 12. Mendel's First Law
```python
## Mendelian Inheritance

# Date : 20.01.07 (Tue)

## 01. Read File

with open("rosalind_iprb.txt", 'r') as f :
	k, m, n = map(int, f.read().split())


## 02. Calculate the Probability

total = k + m + n
deno = total * (total - 1)

sum1 = k * (k - 1) + m * (m - 1) * 0.75
sum2 = k * m * 2 + k * n * 2 + m * n 
nume = sum1 + sum2

result = float(nume / deno)


## 03. Print the Result

print(result)
```
# Link
> [Mendel's First Law](http://rosalind.info/problems/iprb/)
