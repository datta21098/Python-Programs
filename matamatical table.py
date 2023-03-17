#progarms to display Mathematical table
class Tabletest():
    def _init_(self):
        pass
    def input(self):
        self.n=int(input("Enter a number to display the table:"))
    def process(self):
        for i in range(1,11):
            print("{} * {} = {}".format(self.n,i,self.n*i))
d=Tabletest()
d.input()
d.process()

