# 19 Consensus and Profile
```python
## Finding a Most Likely Common Ancestor

# Date : 20.03.14 (Sat)

## 00. Set Variables

string_ls = []
max_ls = []
idx_ls = []

string = ""
consensus = ""
dic = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}


## 01. Read File

with open("rosalind_cons.txt") as f :
	fr = f.read().strip().split("\n")

	for i in range(len(fr)) :
		if fr[i].startswith(">") :

			if string != "" :
				string_ls.append(string)
				string = ""

		else :
			string += fr[i]
			
			if i == (len(fr) - 1):
				string_ls.append(string)


## 02. Create Profile Matrix

prof_len = len(string_ls[0])
profile = [[0 for _ in range(prof_len)] for _ in range(4)]

for x in string_ls :
	for i in range(len(x)) :
		aa = dic[x[i]]
		profile[aa][i] += 1


## 03. Create Consensus String Index

# Create Max List
for i in range(prof_len) :
	tmp_ls = []

	for j in range(4) :
		tmp_ls.append(profile[j][i])

	# Create Index List
	idx_ls.append(tmp_ls.index(max(tmp_ls)))


## 04. Print Consensus String

for x in idx_ls :
	for aa, idx in dic.items() :
		if idx == x :
			consensus += aa
			break

print(consensus)
```
## Link
> [Consensus and Profile](http://rosalind.info/problems/cons/)
