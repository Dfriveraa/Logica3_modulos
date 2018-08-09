
def desencolar(l):
    a=l[0]
    l=l[1:]
    return a,l
class Queue:
    
    def __init__(self):
        self.elements = []
        
    def put(self, d):
        self.elements = self.elements + [d]
        return self
    
    def get(self):
        a,self.elements=desencolar(self.elements)
        return a
    
    def len(self):
        return len(self.elements)