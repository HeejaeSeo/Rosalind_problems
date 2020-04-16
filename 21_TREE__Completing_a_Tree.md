# 21. Completing a Tree
```python
## The Tree of Life

# Date : 20.03.15 (Sun) - Created
# Date : 20.03.16 (Mon) - Completed

## 00. Set Variables

adj_ls = []
tmp_ls = [[0]]


## 01. Define Function

def removeEl(tmp_ls, n1, n2) :
	mini = min(n1, n2)
	maxi = max(n1, n2)

	tmp_ls.remove(tmp_ls[maxi])
	tmp_ls.remove(tmp_ls[mini])


## 02. Read File

with open("rosalind_tree.txt") as f :
	fr = f.read().strip().split("\n")

num = int(fr[0])

for i in range(1, len(fr)) :
	adj_ls.append(fr[i])


## 03. Get the Minimum Number of Edges

num_ls = [str(x) for x in range(1, num + 1)]

for i in range(len(adj_ls)) :
	j = 0
	n1, n2 = adj_ls[i].split(" ")

	while(j < len(tmp_ls)) :
		flag = 0

		# When n1 is Connected
		if n1 in tmp_ls[j]  :
			flag = 1
			tmp_ls[j].append(n2)

			if n2 in num_ls :
				num_ls.remove(n2)

			else :
				for k in range(len(tmp_ls)) :
					if n1 not in tmp_ls[k] and n2 in tmp_ls[k] :
						new_ls = list(set(tmp_ls[j]) | set(tmp_ls[k]))
						tmp_ls.append(new_ls)
						removeEl(tmp_ls, j, k)
						break

		# When n2 is Connected
		if n2 in tmp_ls[j] :
			flag = 1
			tmp_ls[j].append(n1)

			if n1 in num_ls :
				num_ls.remove(n1)

			else :
				for k in range(len(tmp_ls)) :
					if n2 not in tmp_ls[k] and n1 in tmp_ls[k] :
						new_ls = list(set(tmp_ls[j]) | set(tmp_ls[k]))
						tmp_ls.append(new_ls)
						removeEl(tmp_ls, j, k)
						break
			break

		j += 1

	# When None is Connected
	if flag == 0 :
		tmp = [n1, n2]
		tmp_ls.append(tmp)

		num_ls.remove(n1)
		num_ls.remove(n2)


## 04. Print the Number

edge_num = len(num_ls) + len(tmp_ls) - 2
# 1 : for [0] in tmp_ls
# 1 : for the number of lines between elements

print(edge_num)
```
## Link
> [Completing a Tree](http://rosalind.info/problems/tree/)
