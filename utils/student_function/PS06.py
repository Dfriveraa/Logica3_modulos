import numpy as np
class VBinTree(object):
    
    def __init__(self, v):
        self.v = np.r_[[i for i in v]] # copy
        
    def get_height(self):
        i,c=0,0
        while c<len(self.v):
            c += 2**i
            i += 1
        return i-1
    
    def get_level(self, i):
        n = 0
        while sum([2**j for j in range(n)])<=i:
            n+=1
        return n-1
    
    def get_children_positions(self, i):
        return (2*i+1 if 2*i+1<len(self.v) else None,\
                2*i+2 if 2*i+2<len(self.v) else None)
    
    def get_parent_position(self, i):
        assert type(i)==int and i>=0
        return (i-1)/2 if i!=0 else None

    def get_sibling_position(self, i):
        if i==0:
            return None
        return [k for k in self.get_children_positions(self.get_parent_position(i)) if k!=i][0]
  

    def to_indented_string(self, i, level):
        c = self.get_children_positions(i)
        s = (" "*2*level + str(self.v[i]) + "\n") if self.v[i] is not None else ""
        s += self.to_indented_string(c[0],level+1) if c[0] is not None else ""
        s += self.to_indented_string(c[1],level+1) if c[1] is not None else ""
        return s
    
    def __repr__(self):
        return self.to_indented_string(0,0)