# 18. Mortal Fibonacci Rabbits
```python
## Wabbit Seasons

# Date : 20.03.13 (Fri)

## 01. Define Function

def fibo_dyna(n, m) :

	fibo_new = [1, 0]
	fibo_total = [1, 1]

	if n < 2 :
		return fibo_total[n]

	else :
		for i in range(2, n + 1) :
			tmp = 0

			# fibo_new
			for j in range(m - 1) :
				if i >= j + 2 :
					tmp += fibo_new[-(j + 2)]

				else :
					continue

			fibo_new.append(tmp)

			# death
			if i >= m :
				death = fibo_new[i - m]

			else :
				death = 0

			# fibo_total
			fibo_total.append(fibo_total[-1] + fibo_new[-1] - death)

	return fibo_total[n]


## 02. Read File

with open("rosalind_fibd.txt") as f :
	n, m = map(int, f.readline())


## 03. Print Rabbit Pairs

print(fibo_dyna(n - 1, m))
```
## Link
> [Mortal Fibonacci Rabbits](http://rosalind.info/problems/fibd/)
