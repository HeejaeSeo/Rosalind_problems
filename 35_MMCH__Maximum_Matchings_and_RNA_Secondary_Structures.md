# 35. Maximum Matchings and RNA Secondary Structures
```python
## Breaking the Bonds

# Date : 20.04.03 (Fri)

## 00. Define Function

def multi(x, y) :
	answer = 1

	n1 = max(x, y)
	n2 = min(x, y)
	
	for i in range(n2) :
		answer *= n1
		n1 -= 1

	return answer


## 01. Set Variables

seq = ""
base_dic = {'A' : 0, 'U' : 0, 'G' : 0, 'C' : 0}


## 02. Read File

with open("rosalind_mmch.txt") as f :
	fr = f.read().strip().split("\n")

for i in range(1, len(fr)) :
	seq += fr[i]


## 03. Count the Number of Bases

for base, cnt in base_dic.items() :
	base_dic[base] = seq.count(base)


## 04. Calculate the Number of Maximum Matchings

resultAU = multi(base_dic['A'], base_dic['U'])
resultGC = multi(base_dic['G'], base_dic['C'])

result = resultAU * resultGC

print(result)
```
## Link
> [Maximum Matchings and RNA Secondary Structures](http://rosalind.info/problems/mmch/)
