import numpy as np
import itertools
class Graph:
    
    def __init__(self, num_nodes, edge_list, is_directed=False):
        
        assert type(edge_list)==list, "edge_list must be a list of tuples"
        assert type(num_nodes)==int, "num_nodes must be an int"
        
        for t in edge_list:
            assert len(t)==2, "edge_list must be a list of tuples"
            assert t[0]<num_nodes and t[0]>=0 and t[1]<num_nodes and t[1]>=0, "edge number not allowed " + str(t)
        
        self.is_directed = is_directed
        self.num_nodes   = num_nodes
        
        self.nodes ={}
    
        if (is_directed):
            for j in range(num_nodes):
                b=[]
                for i in edge_list:
                    if i[0]==j:
                        b.append(i[1])
                b=list(np.unique(b))
                self.nodes[j]=b
        else:
            for j in range(num_nodes):
                b=[]
                for i in edge_list:
                    if i[0]==j:
                        b.append(i[1])
                    if i[1]==j:     
                        b.append(i[0])
                b=list(np.unique(b))
                self.nodes[j]=b
        
       