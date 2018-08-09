
def append(l,d):
    return l+[d]

def getremove_last(l):
    assert len(l)!=0,"error"
    val=l[-1]
    rest_list=l[:len(l)-1]
    return val, rest_list
    

class Stack:
    
    def __init__(self):
        self.elements = []
  
    def put(self, d):
        self.elements=append(self.elements,d)
        return self
        
    def get(self):
        c,self.elements=getremove_last(self.elements)
        return c

    def len(self):
        return len(self.elements)