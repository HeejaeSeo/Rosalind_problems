# 07. Finding a Motif in a DNA
```python
## Combing Through the Haystack

# Date : 19.10.15 (Tue)

## 01. Read File

with open("rosalind_subs.txt") as f :
	fr = f.readlines()

s = fr[0].replace("\n", "")
t = fr[1].replace("\n", "")


## 02. Find and Print the Motif

for i in range(len(s)) :
	if s[i] == t[0] :
		if s[i : i + len(t)] == t :
			print(i + 1, end = " ")
```
## Link
> [Finding a Motif in DNA](http://rosalind.info/problems/subs/)
