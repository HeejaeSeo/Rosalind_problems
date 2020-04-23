# 24. Inferring mRNA from Protein
```python
## Pitfalls of Reversing Translation

# Date : 20.03.20 (Fri)

## 00. Set Variables

string = ""
result = 3

codon_dic = {
	"F" : 2, "L" : 6, "S" : 6, "Y" : 2, "C" : 2, "W" : 1, "P" : 4, 
	"H" : 2, "Q" : 2, "R" : 6, "I" : 3, "M" : 1, "T" : 4, "N" : 2, 
	"K" : 2, "V" : 4, "A" : 4, "D" : 2, "E" : 2, "G" : 4
	}


## 01. Read File

with open("rosalind_mrna.txt") as f :
	fr = f.read().strip().split("\n")

	for i in range(len(fr)) :
		string += fr[i]


## 02. Get mRNA Sequence from Protein

for i in range(len(string)) :
	result *= codon_dic[string[i]]
	result = result % 1000000

answer = result % 1000000


## 03. Print the Answer

print(answer)
```
## Link
> [Inferring mRNA from Protein](http://rosalind.info/problems/mrna/)
