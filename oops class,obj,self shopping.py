class shopping:
    def dress_type(self,model):
        print("dress_type:",model)
        self.f=model
        print(self.f)
    def price(self,cost):
        print("price:",cost)
        self.s=cost
    def size(self,c):
        print("size:",c)
        self.l=c
        print(self.s)
        print(self.l)
#objname=clsname()
customer=shopping()
#objname.funname()
customer.dress_type("saree")
customer.price(5000)
customer.size(7)
