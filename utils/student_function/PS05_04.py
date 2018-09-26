from PS05 import *
class L4(L):
    def clone(self):    
        def clone_node(node):
            if node==None:
                return None
            return Node(node.value, clone_node(node.next))         
               
        r=L4(clone_node(self.first_node))
        x=r.first_node
        for i in range(len(r)):
            if isinstance(x.value,L4):
                x.value=L4(clone_node(x.value.first_node))
            x=x.next            
        return r