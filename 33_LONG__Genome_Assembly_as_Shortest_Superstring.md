# 33. Genome Assembly as Shortest Superstring
```python
## Introduction to Genome Sequencing

# Date : 20.04.01 (Wed)

## 00. Set Variables

seq_ls = []
tmp_seq = ""


## 01. Read File

with open("rosalind_long.txt") as f :
	fr = f.read().strip().split("\n")

	for i in range(1, len(fr)) :

		if fr[i].startswith(">") :
			seq_ls.append(tmp_seq)
			tmp_seq = ""
		else :
			tmp_seq += fr[i]

	seq_ls.append(tmp_seq)


## 02. Get the Shortest Superstring

std = seq_ls[0]			# standard seq
half = round(len(std) / 2) 	# half length of standard seq
seq_ls.remove(seq_ls[0])	# eliminate standard seq in seq_ls

while(seq_ls) :
	for x in seq_ls :	# seq to repeat

		for j in range(len(x) - half) :		
			if x[j : j + half] in std :
				frag = x[j : j + half]

				start_idx = std.index(frag)
				end_idx = std.index(frag) + half

				prev = max(x[: j], std[: start_idx])
				after = max(x[j + half :], std[end_idx :])

				std = prev + x[j : j + half] + after				
				seq_ls.remove(seq_ls[seq_ls.index(x)])
				break
print(std)
```
## Link
> [Genome Assembly as Shortest Superstring](http://rosalind.info/problems/long/)
