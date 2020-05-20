# 40. Expected Number of Restriction Sites
```python
## A Shot in the Dark

# Date : 20.04.16 (Thu)

## 00. Set Variables

result_ls = []


## 01. Read File

with open("rosalind_eval.txt") as f :
	fr = f.read().strip().split("\n")

n = int(fr[0])
seq = fr[1]
prob_ls = fr[2].split(" ")

seq_len = len(seq)


## 02. Calculate the Probability

for x in prob_ls :
	gc = float(x) / 2
	at = (1 - float(x)) / 2
	result = 1

	for s in seq :
		if s == "A" or s == "T" :
			result *= at
			
		else :
			result *= gc

	result *= (n - seq_len + 1)	# the number of cases where the substring exists
	
	result_ls.append(result)


## 03. Print the Result

for x in result_ls :
	print(x, end = " ")
```
## Link
> [Expected Number of Restriction Sites](http://rosalind.info/problems/eval/)
