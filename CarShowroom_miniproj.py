class car_showroom:
    def _init_(self):
        self.C=0.06
        self.S=0.03
        self.I=21000
    def company(self): 
        while True:
                print("Choose from Maruthi,MG,Hyundai")       
                self.n=input("enter company:")
                if self.n=="Maruthi":
                    print("welcome to",self.n,"car family") 
                    self.models()
                    break
                elif self.n=="MG":
                     print("welcome to",self.n,"car family")
                     self.models()
                     break
                elif self.n=="Hyundai":
                     print("welcome to",self.n,"car family")
                     self.models()
                     break
                else:
                     print("enter valid company")
    def models(self):
        if self.n=="Maruthi":
            while True:
                print("select from Breeza,Baleno")
                self.m=input("enter model:")
                if self.m=="Breeza":
                    self.price()
                    break
                self.m=input("enter model:")
                if self.m=="Baleno":
                    self.price()
                    break
        elif self.n=="MG":
            while True:
                print("select from Hector Plus,Hector")
                self.m=input("enter model:")
                if self.m=="Hector":
                    self.price()
                    break
                self.m=input("enter model:")
                if self.m=="Hector Plus":
                    self.price()
                    break
        elif self.n=="Hyundai":
            while True:
               print("select from Fusion,Escape")
               self.m=input("enter model:")
               if self.m=="Fusion":
                    self.price()
                    break
               self.m=input("enter model:")
               if self.m=="Escape":
                    self.price()
                    break
               self.price()
               break
        else:
                print("invalid company name.")
    def price(self):
            if self.m=="Breeza":
                self.p=1000000 
            elif self.m=="Baleno":
                self.p=2500000
            elif self.m=="Hector Plus":
                self.p=700000
            elif self.m=="Hector":
                self.p=630000
            elif self.m=="Fusion":
                self.p=680000
            elif self.m=="Escape":
                self.p=780000
            total=self.p + self.C + self.S + self.I
            print(total)
obj=car_showroom()
obj.company()
