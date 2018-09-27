import numpy as np

class BTNode:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = None
        self.right = None
        self.parent = None
        if left is not None:
            self.add_left(left)
        if right is not None:
            self.add_right(right)
    
    def add_left(self, value):
        assert self.left is None, "node already has left child"
        self.left  = self.__class__(value) if not isinstance(value,self.__class__) else value
        self.left.parent = self
        return self
        
    def add_right(self, value):
        assert self.right is None, "node already has right child"
        self.right  = self.__class__(value) if not isinstance(value,self.__class__) else value
        self.right.parent = self
        return self
    
    def swap_children(self):
        tmp = self.left
        self.left = self.right
        self.right = self.left
        return self
    
    def insert_ordered(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.add_left(new_value)
                return self.left
            else:
                return self.left.insert_ordered(new_value)
        else:
            if self.right is None:
                self.add_right(new_value)
                return self.right
            else:
                return self.right.insert_ordered(new_value)
        
    def ird(self):
        if self.value==None:
            return []
        s1 = self.left.ird() if self.left is not None else []
        s2 = self.right.ird() if self.right is not None else []
        return s1+[self.value]+s2    
    
    def to_indented_string(self, level, prefix=""):
        s = (" "*2*level + prefix + str(self.value) + "\n") if self.value is not None else ""
        s += self.left.to_indented_string(level+1, prefix="L: ") if self.left is not None else ""
        s += self.right.to_indented_string(level+1, prefix="R: ") if self.right is not None else ""
        return s       

    def __repr__(self):
        return self.to_indented_string(0, prefix="root: ")

    def clone(self):
        r = self.__class__(self.value)
        
        if self.left is not None:
            r.left = self.left.clone()
            r.left.parent = r
        if self.right is not None:
            r.right = self.right.clone()
            r.right.parent = r
        
        return r
    
    @classmethod
    def from_list(cls, a_list):
        r = cls(a_list[0])
        for i in a_list[1:]:
            r.insert_ordered(i)
        return r
    
    @classmethod
    def sort_list(cls, a_list):
        r = cls.from_list(a_list)
        return np.r_[r.ird()]