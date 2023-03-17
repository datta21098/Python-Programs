#program to find factoral of a number using forloop
class fact():
    def __init__(self):
        self.fact=1
        self.c=1
    def accept(self):
        self.n=int(input("Enter a number:"))
    def process(self):
       for i in range(1,self.n):
           self.fact=self.fact*i
    def output(self):
         print("The factoral of ",self.n,"is",self.fact)
d=fact()
d.accept()
d.process()
d.output()
