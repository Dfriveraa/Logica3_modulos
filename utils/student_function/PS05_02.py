from PS05 import *
class L2(L):
    def __setitem__(self, idx, value):
        k = self.first_node
        if idx>=0:
            for i in range(idx):
                assert k.next is not None, "index %s out of range"%(str(idx))
                k = k.next
            k.value=value        
        else:
            for j in range(len(self)+idx):
                assert k.next is not None, "index %s out of range"%(str(idx))
                k = k.next
            k.value=value    
        return k.value
        