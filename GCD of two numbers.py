#program to find GCD of two numbers
class dispGCD():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def process(self):
        while self.a!=self.b:
            if self.a>self.b:
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
        print("GCD is :",self.b)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
d=dispGCD(a,b)
d.process()
            
                
                
