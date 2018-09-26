from PS05 import *
class L5(L):
    
    def clone(self):
        def clone_node(node):
            if node==None:
                return None
            return Node(node.value, clone_node(node.next))         
               
        r=L5(clone_node(self.first_node))
        x=r.first_node
        for i in range(len(r)):
            if isinstance(x.value,L5):
                x.value=L4(clone_node(x.value.first_node))
            x=x.next            
        return r
    
    def __add__(self, M):
        a=self.clone()
        b=M.clone()
        i=a.first_node
        while i.next is not None:
            i=i.next
        i.next=b.first_node        
        return a  
        