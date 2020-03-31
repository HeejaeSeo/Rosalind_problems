# 10 Calculating Protein Mass
```python

## Chaining the Amino Acids

# Date : 20.01.05 (Sun)

## 00. Set Variables

protein = ""


## 01. Read File

with open("rosalind_prtm.txt", 'r') as f :
	fr = f.readlines()

	for i in range(len(fr)) :
		protein += fr[i].replace("\n", "")


## 02. Define Function

def ProteinMass(seq) :
	massTable = {
		'A':'71.03711',
		'C' :'103.00919',
		'D':'115.02694',
		'E':'129.04259',
		'F':'147.06841',
		'G':'57.02146',
		'H':'137.05891',
		'I':'113.08406',
		'K':'128.09496',
		'L':'113.08406',
		'M':'131.04049',
		'N':'114.04293',
		'P':'97.05276',
		'Q':'128.05858',
		'R':'156.10111',
		'S':'87.03203',
		'T':'101.04768',
		'V':'99.06841',
		'W':'186.07931',
		'Y':'163.06333'
	}

	mass = 0
	
	for x in range(seq) :
		mass += float(massTable[x])

	return mass


## 03. Calculate Mass

mass = ProteinMass(protein)
print(mass)
```
## Link
> [Calculating Protein Mass](http://rosalind.info/problems/prtm/)
