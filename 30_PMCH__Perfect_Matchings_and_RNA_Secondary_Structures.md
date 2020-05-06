# 30. Perfect Matchings and RNA Secondary Structures
```python
## Introduction to RNA Folding

# Date : 20.03.27 (Fri)

## 00. Set Variables

cntAU = cntGC = 0
seq = ""


## 01. Read File

with open("rosalind_pmch.txt") as f :
	fr = f.readlines()


## 02. Count the Number of Bases

for i in range(1, len(fr)) :
	seq += fr[i].replace("\n", "")

for x in seq :
	if x == "A" :
		cntAU += 1

	elif x == "G" :
		cntGC += 1


## 03. Calculate the Number of Perfect Matching

factAU = factGC = 1

for i in range(1, cntAU + 1) :
	factAU *= i

for i in range(1, cntGC + 1) :
	factGC *= i

result = factAU * factGC

print(result)
```
## Link
> [Perfect Matchings and RNA Secondary Structures](http://rosalind.info/problems/pmch/)
