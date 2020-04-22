# 25. Finding a Shared Motif
```python
## Searching Through the Haystack

# Date : 20.03.22 (Sun)

## 00. Set Variables

string_ls = []
com_ls = []
string = ""
cnt = 0


## 01. Read File

with open("rosalind_lcsm.txt", 'r') as f :
	fr = f.read().strip().split("\n")

for i in range(1, len(fr)) :
	if fr[i].startswith(">") :
		string_ls.append(string)
		string = ""

	else :
		string += fr[i]

# Add the Last Sequence		
string_ls.append(string)


## 02. Find the Shared Sequences - 1st

s1 = string_ls[0]
s2 = string_ls[1]

for i in range(len(s1) - 1) :
	for j in range(len(s2) - 1) :
		if s1[i : i + 2] == s2[j : j + 2] :
			com_ls.append(s1[i : i + 2])
			x = i + 2
			y = j + 2

			while(x < len(s1) and y < len(s2)) :
				if s1[x] == s2[y] :
					com_ls.append(s1[i : x + 1])
					x += 1
					y += 1
					
				else :
					break


## 03. Find the Shared Sequences - Else

for i in range(2, len(string_ls)) :
	for j in range(len(com_ls) - 1, -1, -1) :
		if com_ls[j] not in string_ls[i] :
			com_ls.remove(com_ls[j])


## 04. Find the Longest Common Substring

for x in com_ls :
	if len(x) > cnt :
		result = x
		cnt = len(x)

print(result)
```
## Link
> [Finding a Shared Motif](http://rosalind.info/problems/lcsm/)
