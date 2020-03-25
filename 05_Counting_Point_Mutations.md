
# 05. Counting Point Mutations
```python

## Evolution as a Sequence of Mistakes

# Date : 19.06.13 (Thu)

## 00. Set Variables

num = 0


## 01. Read File

with open("rosalind_hamm.txt") as f :
	fr = f.readlines()
	
s = fr[0].replace("\n", "")
t = fr[1].replace("\n", "")


## 02. Count the Number of Point Mutations 

length = len(s)

for i in range(length) :
	if (s[i] == t[i]) :
		continue
		
	else :
		num += 1


## 03. Print the Number of Mutations

print(num)
```
## Link
> [Counting Point Mutations](http://rosalind.info/problems/hamm/)
