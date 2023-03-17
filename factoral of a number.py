#program to find fcatoral of a number using while loop
class fact():
    def __init__(self):
        self.fact=1
        self.c=1
    def accept(self):
        self.n=int(input("Enter a number:"))
    def process(self):
        while self.c<=self.n:
            self.fact=self.fact*self.c
            self.c=self.c+1
            print("The factoral of ",self.n,"is",self.fact)
d=fact()
d.accept()
d.process()

