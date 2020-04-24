# 26. Enumerating Oriented Gene Orderings
```python
## Synteny Blocks Have Orientations

# Date : 20.03.23 (Mon)

## 00. Import Library

from itertools import permutations, product


## 01. Set Variables

case1 = 1	# case of permutation
case2 = 1	# whether positive or negative

main_ls = []
pro_ls = []
result_ls = []
idx_ls = [0, 1]


## 02. Read File

with open("rosalind_sign.txt") as f :
	num = int(f.read().strip())


## 03. Calculate the Number of Cases

for i in range(num) :
	case1 *= (i + 1)

for i in range(num) :
	case2 *= 2

case = case1 * case2
print(case)


## 04. Calculate Permutations

for i in range(num) :
	main_ls.append([i + 1, (i + 1) * -1])

pro_idx_ls = list(product(idx_ls, repeat = num))

# Create Combination List
for i in range(len(pro_idx_ls)) :
	tmp_ls = []

	for j in range(num) :
		tmp = pro_idx_ls[i][j]
		tmp_ls.append(main_ls[j][tmp])

	pro_ls.append(tmp_ls)	

# Create Permutation List
for x in pro_ls :
	per_ls = list(permutations(x))

	for y in per_ls :
		result_ls.append(list(y))


## 05. Print the Result

for x in result_ls :
	for i in range(len(x)) :

		if i == num - 1 :
			print(x[i])
		else :
			print(x[i], end = " ")
```
## Link
> [Enumerating Oriented Gene Orderings](http://rosalind.info/problems/sign/)
