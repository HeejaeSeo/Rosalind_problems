### 02. Transcribing DNA into RNA
## The Second Nucleic Acid

# Date : 19.06.12 (Wed)

## 01. Read File

with open("rosalind_rna.txt") as f :
	fr = f.readline()
	fr = fr.replace("\n", "")


## 02. Convert 'T' into 'U'

for s in fr :
	fr  = fr.replace("T", "U")


### 03. Print String

print(fr)