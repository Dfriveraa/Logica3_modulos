import itertools
import numpy as np

def add_to_dict(d, key1, key2, val):
    if d.get(key1)==None:
        d[key1]={}
    d[key1][key2]=val 
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
    
    def T(self):
        w = np.zeros((self.shape[1],self.shape[0]))
        for i in self.rows.keys():
            for j in self.rows[i].keys():
                w[j][i] = self.rows[i][j]
        r = self.__class__(w)        
        return r