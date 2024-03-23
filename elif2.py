hindi=int(input("enter the hindi"))
science=int(input("enter the science"))
history=int(input("enter the history"))
if hindi>80 and science>80 and history>80:
    print("A+")
elif hindi>60 and science>60 and history>60 or hindi<80 and science<80 and history<80:
    print("B+")
else:
    print("pass")
