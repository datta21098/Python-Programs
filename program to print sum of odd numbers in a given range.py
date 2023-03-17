#Aim:Program to print sum of odd numbers
class Display():
    def accept(self):
        self.sum=0
        self.i=int(input("Enter intial value:"))
        self.f=int(input("Enter Finial value:"))
    def process(self):
        while self.i<=self.f:
            if self.i%2!=0:
                print(self.i,end="   ")
                self.sum=self.sum+self.i
            self.i=self.i+1
    def output(self):
        print("\nSum of odd numbers :",self.sum)
d=Display()
d.accept()
d.process()
d.output()
