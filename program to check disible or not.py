#Aim:Program to read a number and check weather it is divisible by 2 and 5
class Display():
    def accept(self):
        self.n=int(input("Enter a number:"))
    def process(self):
        if self.n%2==0 and self.n%5==0:
            print("YES")
        else:
            print("Not Possible")
d=Display()
d.accept()
d.process()
