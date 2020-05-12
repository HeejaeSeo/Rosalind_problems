# 34. Speeding Up Motif Finding
```python
## Shortening the Motif Search

# Date : 20.04.02 (Thu)

## 00. Set Variables

seq = ""


## 01. Read File

with open("rosalind_kmp.txt") as f :
	fr = f.read().strip().split("\n")
  
for i in range(1, len(fr)) :
	seq += fr[i]


## 02. Find the Motif

f_arr = [0 for _ in range(len(seq))]

for i in range(1, len(seq)) :
	idx = 0
	
	if seq[i] == seq[0] :
		x = 2

		if f_arr[i] == 0 :
			f_arr[i] = 1	# when the common motif doesn't exist

		while(i + x < len(seq) + 1) :
			if seq[i : i + x] == seq[0 : x] :
				if f_arr[i + x - 1] < x :
					f_arr[i + x - 1] = x	# add when the common motif doesn't exist
			
			else :
				break

			x += 1

for x in f_arr :
	print(x, end = " ")
```
## Link
> [Speeding Up Motif Finding](http://rosalind.info/problems/kmp/)
