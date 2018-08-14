import numpy as np
from IPython.display import Math
def add_lists(r,a,b):
    while (len(a)<len(b)):
        a=a+[0]
    while(len(a)>len(b)):
        b=b+[0]
    na=np.array(a)
    nb=np.array(b)
    r.coefs=list(na+nb)
    return r
    

class Pol5:
    
    def __init__(self):
        self.coefs = [0]
        
    def add_term(self, c, e):
        s=len(self.coefs)
        if s<=e:
            while s<e+1:
                self.coefs=self.coefs+[0]
                s+=1
            self.coefs[e]=self.coefs[e]+c    
        else :
            self.coefs[e]=self.coefs[e]+c
        return self

    def sum(self, q):
        r=Pol5()
        add_lists(r,self.coefs,q.coefs)
        return r
    
    def show(self):
        s = "+".join(["%s^{%s}"%(str(c) if e==0 else str(c)+"x" if c!=1 else "x", str(e) if e not in [0,1] else "") for e,c in enumerate(self.coefs) if c!=0])
        s = s.replace("+-", "-")
        return Math(s)
    