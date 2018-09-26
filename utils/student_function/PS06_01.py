import PS06
class VBinTree(PS06.VBinTree):
    
    def shift_down(self, start, end=None):
        end = len(self.v)-1 if end is None else end
        root = start
        aux = self.v[root]
        while (self.get_children_positions(root)[0] is not None) and self.get_children_positions(root)[0]<=end :   
            if((2*root+2)>end):
                if(aux < self.v[2*root+1]):
                    self.v[root] = self.v[2*root+1]
                    self.v[2*root+1] = aux
                root = 2*root+1
            else:
                if (aux < self.v[2*root+1] or aux < self.v[2*root+2]):
                    if (self.v[2*root+1] == self.v[end] and self.v[root] < self.v[2*root+1]):
                        self.v[root] = self.v[end]
                        self.v[2*root+1] = aux
                        root = 2*root+1
                    elif (self.v[2*root+1] > self.v[2*root+2]):
                        self.v[root] = self.v[2*root+1]
                        self.v[2*root+1] = aux
                        root = 2*root+1
                    else:
                        self.v[root] = self.v[2*root+2]
                        self.v[2*root+2] = aux
                        root = 2*root+2
                else:
                    return self
        return self