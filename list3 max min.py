l=[42,36,28,96,4,-1,1]
min=l[0]
max=l[0]
for i in l:
    if i<min:
        min=i
    if i>max:
        max=i
print(min)
print(max)
print(max+min)
