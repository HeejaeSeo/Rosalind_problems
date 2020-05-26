# 42. Ordering Strings of Varying Length Lexicographically
```python
## Organizing Strings of Different Lengths

# Date : 20.05.25 (Mon)

## 00. Set Variables

total_ls = []
seq = ""


## 01. Define Function

def lex(seq, cnt) :

	if cnt > 0 :
		for i in range(length) :
			tmp = seq
			tmp += string[i]
			print(tmp)
			lex(tmp, cnt - 1)
	else :
		return(seq)


## 02. Read File

with open("rosalind_lexv.txt") as f :
	fr = f.read().strip().split("\n")

string = fr[0].split(" ")
num = int(fr[1])
length = len(string)


## 03. Call the Function

lex(seq, num)
```
## Link
> [Ordering Strings of Varying Length Lexicographically](http://rosalind.info/problems/lexv/)
