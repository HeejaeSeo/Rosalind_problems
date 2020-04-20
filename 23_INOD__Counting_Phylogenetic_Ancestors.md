# 23. Counting Phylogenetic Ancestors
```python
## Culling the Forest

# Date : 20.03.18 (Wed) - Posted

## 01. Read File

with open("rosalind_inod.txt") as f :
	leaf_cnt = f.read().strip().replace("\n", "")


## 02. Print the Number of Nodes

internal_node_cnt = int(leaf_cnt) - 2
print(internal_node_cnt)
```
## Link
> [Counting Phylogenetic Ancestors](http://rosalind.info/problems/inod/)
