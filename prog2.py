#program to display vandataram 10times using class
class Display():
#constructor
    def __init__(self):
        self.c=1
    def process(self):
        while self.c<=10: #using self the varible becoms local varable
            print("VandeaMatram #",self.c)
            self.c=self.c+1
#instatite object
d=Display()
d.process()
