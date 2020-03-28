# 08. Overlap Graphs
```python
##  A Brief Introduction to Graph Theroy

# Date : 19.10.16 (Wed)

## 00. Set variables

data_ls = []
id_ls = []
seq_ls = []


## 01. Read File

with open("rosalind_grph.txt") as f :
    fr = f.readlines()

    for x in fr :
        data_ls.append(x.replace("\n", ""))


## 02. Create id_seq_list

data_ls_len = len(data_ls)

for i in range(data_ls_len) :

    # Create id list
    if i % 3 == 0 :
        data_ls[i] = data_ls[i].replace(">","")
        id_ls.append(data_ls[i])

    # Create seq list
    if i % 3 == 1 :
        join = data_ls[i] + data_ls[i + 1]
        seq_ls.append(join)


## 03. Print Overlap Strand ID

id_ls_len = len(id_ls)

for i in range(id_ls_len - 1) :

    for j in range(id_ls_len - 1) :

        if i != j :
            if seq_ls[i][-3 :] == seq_ls[j][0 : 3] :
                print("%s %s" %(id_ls[i], id_ls[j]))
```
## Link
> [Overlap Graphs](http://rosalind.info/problems/grph)
