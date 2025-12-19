# Area of rectangle using oops
class rect:
    def __init__(self,L,B):
        self.L = L
        self.B = B
        def arearect(self):
            return self.L*self.B

#driver code
L,B=int(input("enter L,B"))

t=rect(5,6)

a=t.arearect()
              
