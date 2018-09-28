import numpy as np
class Graph:
    def __init__(self, num_nodes, edge_list):
        assert type(edge_list)==list, "edge_list must be a list of tuples"
        assert type(num_nodes)==int, "num_nodes must be an int"
        
        for t in edge_list:
            assert len(t)==2, "edge_list must be a list of tuples"
            assert t[0]<num_nodes and t[0]>=0 and t[1]<num_nodes and t[1]>=0, "edge number not allowed " + str(t)
            
        self.num_nodes   = num_nodes
        self.inc_matrix=np.zeros((num_nodes,len(edge_list)),int)
        a=0
        for i,j in edge_list:
            self.inc_matrix[i][a]=1
            self.inc_matrix[j][a]=1
            a+=1
    
    def assert_valid_node_number(self, n):
        assert n>=0 and n<self.num_nodes, "invalid node number: %d"%n        
    
    def grade(self, node_number):
        self.assert_valid_node_number(node_number)
        
        return self.inc_matrix.sum(axis=1)[node_number] 
    
    def are_adyacent(self, node_number_1, node_number_2):
        self.assert_valid_node_number(node_number_1)
        self.assert_valid_node_number(node_number_2)
        
        for a in range(self.inc_matrix.shape[1]):
            if self.inc_matrix[node_number_1][a]==1 and self.inc_matrix[node_number_2][a]==1:return True
        return False
        
    def is_valid_trayectory(self, trayectory):
        assert type(trayectory)==list, "trayectory must be a list"
        for i in range(len(trayectory)-1):
                if not self.are_adyacent(trayectory[i],trayectory[i+1]):return False
        
        return True