n=12467
cnt=0
while n>0:
    d=n%10
    if d%2==0:
       cnt=cnt+1
    n=n//10
print(cnt)
