# 11. Finding a Spliced Motif
```python
## Motifs are Rarely Contiguous

# Date : 20.01.07 (Tue)

## 00. Set Variables

start = 0
flag = 0
s = ""
idx_ls = []


## 01. Read File

with open("rosalind_sseq.txt", 'r') as f :
	fr = f.readlines()

	for i in range(1, len(fr)) :
		fr[i] = fr[i].replace("\n", "")

		if fr[i].startswith(">") == 0 :
			s += fr[i]

		else :
			break

	t = fr[len(fr) - 1]


## 02. Create Index

s_len = len(s)
t_len = len(t)


for i in range(t_len) :
	flag = 0

	for j in range(start, s_len) :

		if flag == 0 and t[i] == s[j] :
			idx_ls.append(j)
			start = j + 1
			flag = 1


## 03. Print Index List

for x in idx_ls :
	print(x + 1, end = ' ')
```
## Link
> [Finding a Spliced Motif](http://rosalind.info/problems/sseq/)
