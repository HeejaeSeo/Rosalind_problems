# 28. Introduction to Random Strings
```python
## Modeling Random Genomes

# Date : 20.03.25 (Wed)

## 00. Import Library

import math


## 01. Set Variables

string = ""
prob_ls = []
base_ls = ['A', 'T', 'G','C']


## 02. Define Function

def calProb(x, string) :
	prob = 1
	probG = x / 2
	probA = (1 - x) / 2

	for i in range(len(string)) :
		if string[i] == "A" or string[i] == "T" :
			prob *= probA

		else :
			prob *= probG

	result = round(math.log10(prob), 4)

	return result


## 03. Read File

with open("rosalind_prob.txt") as f :
	fr = f.read().strip().split("\n")

for seq in fr :

	# Sequence
	if seq[0] in base_ls :
		string += seq

	# Probability
	else :
		tmp_ls = seq.split(" ")
		for y in tmp_ls :
			prob_ls.append(float(y))


## 04. Calculate

a = calProb(prob_ls[0], string)

for x in prob_ls :
	print(calProb(x, string), end = " ")
```
## Link
> [Introduction to Random Strings](http://rosalind.info/problems/prob/)
