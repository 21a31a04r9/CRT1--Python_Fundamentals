dict={34:"hi",40:"oh",50:"oops"}
print(dict)
dict[40]="ok"
print(dict)
dict[20]="omg"
print(dict)
print(dict[50])
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)
for x,y in dict.items():
    print(x,y)
dict.pop(40)
print(dict)
