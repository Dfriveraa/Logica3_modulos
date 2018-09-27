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
        
    def get_last_parent_position(self):
        for i in range(len(self.v)-1,-1,-1):
               if (self.get_children_positions(i)[0] is not None or self.get_children_positions(i)[1] is not None ):
                return i

        return None
    
    def make_heap(self):
        end=self.get_last_parent_position()
        for i in range(end,-1,-1):
            self.shift_down(i)
        return self       

                
    def sort(self):
        end = len(self.v)-1
        self.make_heap()
        for i in range(end, -1, -1):
            self.v[i], self.v[0] = self.v[0], self.v[i]
            self.shift_down(0,i-1)
        return self
        
    