def prime():
    a=1
    n=int(input("enter num"))
    for i in range(2,n):
        if n%i==0:
            a=0
            break
    if a==1:
        print("prime")
    else:
        print("not")
prime()
