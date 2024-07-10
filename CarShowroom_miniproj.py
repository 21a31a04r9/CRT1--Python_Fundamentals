class carshowroom:
    def _init_(self,cgst,sgst,insurance):
        self.c=cgst
        self.s=sgst
        self.i=insurance
        print(self.c,self.s,self.i)
    def company(self,name):
        self.n=name
        print("welcome to ",self.n,"family")
    def model(self):
        a="maruthi"
        b="MG"
        c="hyundai"
        a1="X"
        a2="y"
        b1="Z"
        b2="I"
        c1="O"
        c2="H"
        if self.n==a:
            print(a1)
            print(a2)
        elif self.n==b:
            print(b1)
            print(b2)
        elif self.n==c:
            print(c1)
            print(c2)
        else:
            exit
    t=input("company")

    def price(self):
        if self.n==a and t==a1:
            cost1=25
            print(cost1+self.s+self.c+self.i)
        elif self.n==a and t==a2:
            cost2=30
            print(cost2+self.c+self.s+self.i)
        elif self.n==b and t==b1:
            cost3=40
            print(cost3+self.s+self.c+self.i)
        elif self.n==b and t==b2:
            cost4=50
            print(cost4=self.s+self.c+self.i)
        elif self.n==c and t==c1:
            cost5=60
            print(cost5+self.s+self.c+self.i)
        elif self.n==c and t==c2:
            cost6=70
            print(cost7=self.s+self.c+self.i)
p=carshowroom(1,2,3)
p.company("MG")
p.model()
p.price()
