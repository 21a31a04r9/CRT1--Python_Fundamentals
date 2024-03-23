def prime():
    a=int(input("enter value"))
    for n in range(2,a):
        if a%n==0:
            print("not prime")
            break
        else:
            print("prime")
prime()
