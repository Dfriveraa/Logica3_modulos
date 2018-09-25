from PS05 import *
class L1(L):
    def __getitem__(self, idx):
        k = self.first_node
        if idx >=0:
            for i in range(idx):
                assert k.next is not None, "index %s out of range"%(str(idx))
                k = k.next
        else:
            lenNegative=(len(self)*-1)
            assert idx>=lenNegative, "te pasas we"
            for i in range(len(self)+idx):
                assert k.next is not None, "index %s out of range"%(str(idx))
                k = k.next  
        return k.value