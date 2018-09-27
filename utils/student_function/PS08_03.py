import numpy as np
import networkx as nx
class Graph():

    def __init__(self, num_nodes, edge_list, is_directed=False):
        assert type(edge_list)==list, "edge_list must be a list of tuples"
        assert type(num_nodes)==int, "num_nodes must be an int"
        
        for t in edge_list:
            assert len(t)==2, "edge_list must be a list of tuples"
            assert t[0]<num_nodes and t[0]>=0 and t[1]<num_nodes and t[1]>=0, "edge number not allowed " + str(t)
        self.edge_list=edge_list
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
    
    def assert_valid_node_number(self, n):
        assert n>=0 and n<self.num_nodes, "invalid node number: %d"%n        
    
    def grade(self, node_number):
       
        self.assert_valid_node_number(node_number)
        return len(self.nodes[node_number])
    
    def grade_out(self, node_number):
        assert self.is_directed, "only directed graphs have in/out grades"
        self.assert_valid_node_number(node_number)     
        return len(self.nodes[node_number])

    def grade_in(self, node_number):
        assert self.is_directed, "only directed graphs have in/out grades"
        self.assert_valid_node_number(node_number)
        aux=[]
        for i in range(len(self.nodes)):
            aux=aux+self.nodes[i]
        return aux.count(node_number)

    def are_adyacent(self, node_number_1, node_number_2):
        self.assert_valid_node_number(node_number_1)
        self.assert_valid_node_number(node_number_2)
        if node_number_2 in self.nodes[node_number_1] or node_number_1 in self.nodes[node_number_2]:
            return True
        return False
        
    def is_valid_trayectory(self, trayectory):
        assert type(trayectory)==list, "trayectory must be a list"  
        for i in range(len(trayectory)-1):
            if not self.are_adyacent(trayectory[i],trayectory[i+1]):return False
        return True
    
    def as_nx(self):
        if (self.is_directed):
             g=nx.DiGraph(self.nodes)
        else:
            g=nx.Graph(self.nodes)
           
        return g
    
    def draw(self):
        ng = self.as_nx()
        nx.drawing.draw(ng, arrows=self.is_directed, with_labels=True, 
                        node_alpha=.2, node_color="blue", 
                        node_size=900, font_color="white")