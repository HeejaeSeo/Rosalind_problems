# 22. Creating a Distance Matrix
```python
## Introduction to Distance-Based Phylogeny

# Date : 20.03.17 (Tue)

## 00. Set Variables

string_ls = []
tmp = ""


## 01. Read File

with open("rosalind_pdst.txt") as f :
	fr = f.read().strip().split("\n")

# Concatenate Sequences
for i in range(1, len(fr)) :

	if fr[i].startswith(">") == True :
			string_ls.append(tmp)
			tmp = ""

	else :
		tmp += fr[i]

# For the Last Sequence
string_ls.append(tmp)


## 02. Create a Distance Matrix

str_cnt = len(string_ls)
str_len = len(string_ls[0])

pro_arr = [[0 for _ in range(str_cnt)] for _ in range(str_cnt)]

for i in range(str_cnt) :
	for j in range(i + 1, str_cnt) :
		tmp_sum = 0

		for k in range(0, str_len) :
			if string_ls[i][k] != string_ls[j][k] :
				tmp_sum += 1

		tmp_pro = round(tmp_sum / str_len, 5)
		pro_arr[i][j] = pro_arr[j][i] = tmp_pro


## 03. Print the 2-Dimensional List

for x in pro_arr :
	for y in x :
		print(y, end = " ")
	print("")
```
## Link
> [Creating a Distance Matrix](http://rosalind.info/problems/pdst/)
