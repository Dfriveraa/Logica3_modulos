from PS05 import *
class L6(L):
    
    def __eq__(self, other):
            
        a=self.first_node;b=other.first_node
        if len(self) !=len(other):return False
        for i in range(len(self)):
            if a.value!=b.value:return False
            a=a.next;b=b.next
        return True 
    
    def __ne__(self, other):
        return not self==other       