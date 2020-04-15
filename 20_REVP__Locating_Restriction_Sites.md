# 20. Locating Restriction Sites
```python
## The Billion-Year War

# Date : 20.03.15 (Sun)

## 00. Set Variables

string = ""
dic = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}


## 01. Define Function

def isPalindrome(i, k) :
	n = 0

	while(n * 2 < k) :
		if(dic[string[i + n]] == string[i + k - n]) :
			n += 1

		else :
			return False

	return True


## 02. Read File

with open("rosalind_revp.txt") as f :
	fr = f.read().strip().split("\n")

	for i in range(1, len(fr)) :
		string += fr[i]
				

## 03. Find Palindrome Position & Length

for k in range(3, 12, 2) :
	for i in range(len(string) - k) :
		if isPalindrome(i, k) == True :
			print(i + 1, k + 1)
```
## Link
> [Locating Restriction Sites](http://rosalind.info/problems/revp/)
