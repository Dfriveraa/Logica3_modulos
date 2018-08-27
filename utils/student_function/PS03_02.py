import itertools

def add_to_dict(d, key1, key2, val):
    if d.get(key1)==None:
        d[key1]={}
    d[key1][key2]=val 
    return d

class SparseMatrix:
    
    def __init__(self, m=None):
        self.rows = {}
        self.shape =m.shape if m is not None else(0,0)
        if m is not None:
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if m[i,j]!=0:
                        add_to_dict(self.rows,i,j,m[i][j])
                           
    def sparseness_metric(self):
        j=0
        for i in self.rows.keys():
            j+=len(self.rows[i])

        metric = (j*1.)/(self.shape[0]*self.shape[1])
        return metric
        