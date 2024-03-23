class placements:
    def info(self):
        print("1062")
class dept(placements):
    def display(self):
        print("all depts")
class pragati(dept):
    def welcome(self):
        print("welcome")
obj=pragati()
obj.info()
