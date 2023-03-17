#Aim:Program to print odd number in a given range
class Displayodd():
    def accept(self):
        self.i=1
        self.f=int(input("Enter finial number:"))
    def process(self):
        while self.i<=self.f:
            if self.i%2!=0:
                print(self.i,end=" ")
            self.i=self.i+1
d=Displayodd()
d.accept()
d.process()
