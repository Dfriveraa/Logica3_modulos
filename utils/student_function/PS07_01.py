import PS07
class BTNode(PS07.BTNode):
    
    def height(self):
        if self is None:return 0
        alturaIzquierda=0;alturaDerecha=0
        if self.left is not None:alturaIzquierda=self.left.height()
        if self.right is not None:alturaDerecha=self.right.height()
        if alturaIzquierda>alturaDerecha:return alturaIzquierda+1
        else: return alturaDerecha+1
    
   
    def balance_factor(self):
        
    
        a=self.left.height()
        
        b=self.right.height()
        result=(a-b)   
        return result
    
    def balance_factor_tree(self):
        r = self.__class__(self.balance_factor(), \
                           left=self.left.balance_factor_tree() if self.left is not None else None,
                           right=self.right.balance_factor_tree() if self.right is not None else None,
                          )
        return r     