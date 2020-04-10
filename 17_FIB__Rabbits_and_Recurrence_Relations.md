# 17. Rabbits and Recurrence Relation
```python
## Wascally Wabbits

# Date : 20.03.10 (Tue)

## 01. Define Function

def fibo_dyna(n, k) :

	fibo_new = [0, 0]
	fibo_total = [0, 1]

	if n < 2 :
		return fibo_total[n]

	else :
		for i in range(2, n + 1) :
			fibo_new.append(fibo_total[i - 2] * k)
			fibo_total.append(fibo_total[-1] + fibo_new[-1])

	return fibo_total[n]


## 02. Read File

with open("rosalind_fib.txt") as f :
	n, k = map(int, f.readline().strip().split(" "))


## 03. Print the Rabbit Pairs

print(fibo_dyna(n, k))
```
## Link
> [Rabbits and Recurrence Relations](http://rosalind.info/problems/fib/)
