def prime(a):
    for n in range(2,a):
        if a%n==0:
            print("not prime")
            break
        else:
            print("prime")
prime(3)
