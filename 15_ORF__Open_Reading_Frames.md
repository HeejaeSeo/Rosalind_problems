# 15. Open Reading Frames
```python
## Transcription May Begin Anywhere

# Date : 20.03.08 (Sun)

## 00. Set Variables

seq = ""
seq_rev_com = ""
prot_ls = []
com_dic = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}


## 01. Define Function

# Translate
def translate(seq):  
	table = { 
		'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
		'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
		'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
		'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
		'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
		'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
		'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
		'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
		'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
		'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
		'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
	}

	protein = ""

	for i in range(0, len(seq), 3): 

		if i + 2 < len(seq) :
			codon = seq[i : i + 3]

			if table[codon] == "_" :
				return protein

			else :
				protein += table[codon]

		else :
			break

# Get the Complementary Sequence
def comp(seq) :
	string_new = ''

	for x in seq :
		string_new += com_dic[x]

	return string_new

# Synthesize
def synthesis(string) :
	for i in range(len(string) - 2) :
		if string[i : i + 3] == "ATG" :
			protein = translate(string[i :])
			if protein != None :
				prot_ls.append(protein)


## 02. Read File

with open("rosalind_orf.txt", 'r') as f :
	fr = f.read().strip().split("\n")


## 03. Concatenate Sequences

for i in range(1, len(fr)) :
	seq += fr[i]

seq_rev = seq[::-1]
seq_com = comp(seq)
seq_rev_com = comp(seq_rev)


## 04. Translate Sequences

synthesis(seq)
synthesis(seq_rev_com)

prot_ls = sorted(list(set(prot_ls)))


## 05. Print Proteins

for x in prot_ls :
	print(x)
```
## Link
> [Open Reading Frames](http://rosalind.info/problems/orf/)
