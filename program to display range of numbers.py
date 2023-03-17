#aim:program to print a range of number
class Displayrange():
    def accept(self):
        self.c=int(input("Enter  initial number:"))
        self.d=int(input("Ente finial number:"))
    def proces(self):
        while self.c<=self.d:
            print(self.c,end="")
            self.c=self.c+1
            
d=Displayrange()
d.accept()
d.proces()
