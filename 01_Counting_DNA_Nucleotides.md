# 01. Counting DNA Nucleotides
```python
## A rapid Introduction to Molecular Biology

# Date : 19.06.12 (Wed)

## 01. Read File

with open("rosalind_dna.txt") as f :
	fr = f.readline()
	fr = fr.replace("\n", "")


## 02. Count the Number of Bases

cnt_a = fr.count("A")
cnt_c = fr.count("C")
cnt_g = fr.count("G")
cnt_t = fr.count("T")


## 03. Print the Number of Bases

print("%d %d %d %d" %(cnt_a, cnt_c, cnt_g, cnt_t))
```
