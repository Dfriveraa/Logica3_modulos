class Node:
    def __init__(self, value, next=None):
        assert next is None or isinstance(next,Node), "next must be Node, not %s"%(type(next))
        self.value = value
        self.next  = next
        
    def __repr__(self):
        return str(self.value)
    
class L(object):
    def __init__ (self, first_node=None):
        assert first_node is None or isinstance(first_node,Node), "first must be Node, not %s"%(type(first_node))
        self.first_node = first_node
        
    def __getitem__(self, idx):
        k = self.first_node
        for i in range(idx):
            assert k.next is not None, "index %s out of range"%(str(idx))
            k = k.next  
        return k.value
    
    def __len__(self):
        k = self.first_node
        if k is None:
            return 0
        i=1
        while k.next is not None:
            i+=1
            k = k.next
        return i
            
    def __repr__ (self):
        if self.first_node is None:
            return "[]"
        
        s = "[ %s"%self.first_node
        k=self.first_node
        while (k.next is not None):
            s += ", %s"%k.next
            k = k.next
    
        return s+" ]"