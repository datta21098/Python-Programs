#Aim:program to display n times vandaemataram using class
class Displayntimes():
    def __init__(self):
        self.c=1
    def Accept(self):
        self.n=int(input("Enter number to display vm:"))
    def process(self):
        while self.c<=self.n:
            print("VandaMatram #",self.c)
            self.c=self.c+1
d=Displayntimes()
d.Accept()
d.process()
