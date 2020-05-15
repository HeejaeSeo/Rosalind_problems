# 37. Introduction to Set Operations
```python
## Forming New Sets

# Date : 20.04.08 (Wed)

## 01. Read File

with open("rosalind_seto.txt") as f :
	fr = f.readlines()
	num = int(fr[0].replace("\n", ""))


## 02. Create Subsets and a Total Set

A_ls = fr[1].replace("{", "").replace("}", "").split(",")
B_ls = fr[2].replace("{", "").replace("}", "").split(",")

A = set([int(x) for x in A_ls])
B = set([int(x) for x in B_ls])

total_ls = [x for x in range(1, num+ 1)]
C = set(total_ls)


## 03. Calculate Set Operations and Print the Result

r1 = A | B
r2 = A & B
r3 = A - B
r4 = B - A
r5 = C - A
r6 = C - B

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
```
## Link
> [Introduction to Set Operations](http://rosalind.info/problems/seto/)
