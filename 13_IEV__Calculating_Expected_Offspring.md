# 13. Calculating Expected Offspring
```python
## The Needs for Averages

# Date : 20.01.08 (Wed)

## 00. Set Variables

# the list of probabilities that offspring will represent dominant phenotype according to their parents' genotypes
ls_prob = [1, 1, 1, 3/4, 1/2, 0]
ls_factor = []
result = 0


## 01. Read File

with open("rosalind_iev.txt", 'r') as f :
	ls_factor = list(map(int, f.read().split()))


## 02. Calculate Expectation Mean

num = len(ls_prob)

for i in range(num) :
	result += ls_prob[i] * ls_factor[i]

result *= 2 # because every couple has 2 offsprings

print(result)
```
## Link
> [Calculating Expected Offspring](http://rosalind.info/problems/iev/)
