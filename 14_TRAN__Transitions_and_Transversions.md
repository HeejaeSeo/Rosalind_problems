# 14. Transitions and Transversions
```python
## Certain Point Mutations are More Common

# Date : 20.01.25 (Sat)

## 00. Set Variables

seq1 = seq2 = ""
transition = transversion = 0
flag = 0


## 01. Read File

with open("rosalind_tran.txt") as f :
	fr = f.read().strip().split("\n")

# Concatenate Each Sequence
for seq in fr :
	if seq.startswith(">") == 1 :
		flag += 1

	else :
		if flag == 1 :
			seq1 += seq

		if flag == 2 :
			seq2 += seq


## 02. Calculate the Ratio of (Transition / Transversion)

length = len(seq1)

for i in range(length) :

	if seq1[i] != seq2[i] :
		tmp_ls = sorted([seq1[i], seq2[i]])

		if tmp_ls == ['A', 'G'] or tmp_ls == ['C', 'T'] :
			transition += 1

		else :
			transversion += 1

result = round(float(transition / transversion), 3)

print(result)
```
# Link
> [Transitions and Transversions](http://rosalind.info/problems/tran/)
