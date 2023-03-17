#program to find prime or not prime
class Primenumber():
    def __init__(self):
        self.c=1
        self.r=1
    def accept(self):
        self.n=int(input("Enter a number to check prime or not:"))
    def process(self):
        while (self.c<=self.n//2) and self.r>=0:
            self.r=self.n%self.c
            self.c=self.c+1
    def condition(self):
        if self.r!=0:
            print(self.n,"Prime")
        else:
            print(self.n,"Not      Prime")

d=Primenumber()
d.accept()
d.process()
d.condition()
 
