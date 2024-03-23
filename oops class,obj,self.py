class f15:
    def light(self):
        print("ok switching on the lights")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
#objname=clsname()
bindu=f15()
#objname.funname()
bindu.light()
bindu.fan(5)
bindu.cpu()
