# 44. Comparing Spectra with the Spectral Convolution
```python
## Comparing Spectra

# Date : 20.05.29 (Fri)

## 00. Set Variables

ans_dic = {}


## 01. Read File

with open("rosalind_conv.txt") as f :
	fr = f.read().split("\n")

	s1 = fr[0].split(" ")
	s2 = fr[1].split(" ")


## 02. Get the Highest Frequency Value

for x in s1 :
	for y in s2 :

		X = float(x)
		Y = float(y)

		if X >= Y :
			tmp = round(X - Y, 5)

			if str(tmp) in ans_dic :
				ans_dic[str(tmp)] += 1

			else :
				ans_dic[str(tmp)] = 1


## 03. Print the Result

for n, v in ans_dic.items() :
	if v == max(ans_dic.values()) :
		print(v)
		print(n)
```
## Link
> [Comparing Spectra with the Spectral Convolution](http://rosalind.info/problems/conv/)
