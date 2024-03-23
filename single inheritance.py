class f15:
    def light(self):
        print("ok switching on the lights")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
class shopping(f15):
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
