from PS05 import *

def clone_node(node):
    if(node == None):
        return None    
    return Node(node.value, clone_node(node.next))