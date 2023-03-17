#aim:program to print a range of number
class Displayrange():
    def accept(self):
        self.c=int(input("Enter  initial number:"))
        self.d=int(input("Ente finial number:"))
    def proces(self):
        while self.d>=self.c:
            print(self.d,end="")
            self.d=self.d-1
            
d=Displayrange()
d.accept()
d.proces()
