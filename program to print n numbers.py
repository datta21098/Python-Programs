class Display():
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("Ente a number:"))
    def process(self):
        while self.c<=self.n:
            print(self.c,end="")
            self.c=self.c+1
d=Display()
d.accept()
d.process()
