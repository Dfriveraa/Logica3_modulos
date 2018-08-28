
import itertools
import numpy as np
def add_to_dict(d, key1, key2, val):
    if key1 in d.keys():
            d[key1][key2] = val
    else:
        d[key1] = {key2: val}
    
    return d

class SparseMatrix:
    
    def __init__(self, m=None):
        self.rows = {}
        self.shape = m.shape if m is not None else (0,0)
        self.nb_elements = 0
        
        if m is not None:
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if m[i,j] != 0:
                        add_to_dict(self.rows, i, j, m[i,j])
                        self.nb_elements = self.nb_elements + 1

    def to_dense(self):
        r = np.zeros(self.shape)
        
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                r[i][j] = self.rows[i][j]
            
        return r
                        
    def __getitem__(self, (i,j)):
        assert i<= (self.shape[0]-1), "Indices fuera de la matriz"
        assert j<= (self.shape[1]-1), "Indices fuera de la matriz"
            
        for n in self.rows.keys():
            for m in self.rows[n].keys():
                if n == i and m == j:
                    return self.rows[n][m]
                
        return 0
    
    def __setitem__(self, (i,j), val):
        if val != 0:
            add_to_dict(self.rows, i, j, val)
            
            if i > (self.shape[0]-1):
                self.shape=((i+1),(self.shape[1]))
            
            if j > (self.shape[1]-1):
                self.shape=((self.shape[0]),(j+1))

    def __add__ (self, q):
        assert self.shape[0] == q.shape[0], "Matrices de diferente tamano"
        assert self.shape[1] == q.shape[1], "Matrices de diferente tamano"

        r = self.__class__()
        r.shape = self.shape
        
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                r[i,j] = self[i,j]
                
        for i in q.rows.keys():
            for j in q.rows[i].keys():
                r[i,j] = r[i,j] + q[i,j]
        
        return r
    
    def dot(self, q):
        assert self.shape[1]==q.shape[0]
        
        
        r = self.__class__()
        r.shape = (self.shape[0] , q.shape[1])
        trans = q.T()
        
        for i in self.rows.keys():
            for j in trans.rows.keys():
                dot_product_one_point = 0
                for k in q.rows.keys():
                    tt = self.rows[i].get(k, 0)
                    dot_product_one_point = dot_product_one_point + tt * trans.rows[j].get(k, 0)
                r[i,j] = dot_product_one_point
        
        
              
        
        return r
    
    def sparseness_metric(self):
        metric = self.nb_elements*1./(self.shape[0]*self.shape[1])
        return metric
    
    def T(self):
        w = np.zeros((self.shape[1],self.shape[0]))
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                w[j][i] = self.rows[i][j]
        
        r = self.__class__(w)
                
        return r