import PS06
class VBinTree(PS06.VBinTree):
        
    def get_last_parent_position(self):
        for i in range(len(self.v)-1,-1,-1):
               if (self.get_children_positions(i)[0] is not None or self.get_children_positions(i)[1] is not None ):
                return i

        return None