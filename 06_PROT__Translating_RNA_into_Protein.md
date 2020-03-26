# 06. Translating RNA into Protein
```python
## The Genetic Code

# Date : 19.06.13 (Thu)

## 00. Define Function 

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
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein = ""

    if len(seq) % 3 == 0 : 
        for i in range(0, len(seq), 3) : 
            codon = seq[i : i + 3] 
            protein += table[codon] 
            
    return protein


## 01. Read File

with open("rosalind_prot.txt", 'r') as f :
    fr = f.readline()
    fr = fr.replace("\n", "")


## 02. Translate 

strand = fr.replace("U", "T")
strand_trans = translate(strand)


## 03. Print Protein String

print(strand_trans)

```
## Link
> [Translating RNA into Protein](http://rosalind.info/problems/prot/)
