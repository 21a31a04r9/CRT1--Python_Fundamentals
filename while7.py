n=123
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
if n%s==0:
    print("divisible")
else:
    print("not")

