# 04. Computing GC Content

```python
## Identifying Unknown DNA Quickly

# Date : 19.06.13 (Thu)

## 00. Set Variables

data = [0, 0, 1, 0]
best = ['name', 0]
cnt_c = cnt_g = 0


## 01. Read File

with open('rosalind_gc.txt') as f :
    for s in f :      
        if s.startswith(">") :
            data[3] = data[1] / data[2] * 100

            if data[3] > best[1] :
                best[0] = data[0]
                best[1] = data[3]
                
            data[0] = s
            data[1] = 0
            data[2] = 0
            cnt_c = cnt_g = 0

        else :
            cnt_c = s.count("C")
            cnt_g = s.count("G")
            data[1] = data[1] + cnt_c + cnt_g
            data[2] += len(s.rstrip('\n'))


## 02. Get GC Content

data[3] = data[1] / data[2] * 100

if data[3] > best[1] :
    best[0] = data[0]
    best[1] = data[3]
                
print(best[0])
print(best[1])
```
## Link
> [Computing GC Content](http://rosalind.info/problems/gc/)
