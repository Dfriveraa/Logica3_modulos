import PS07
class BTNode(PS07.BTNode):
    
    def height(self):
        alturaIzquierda=0;alturaDerecha=0
        if((self.left is None) and (self.right is None)):return 0
        if self.left is not None:
            alturaIzquierda=self.left.height()+1
        if self.right is not None:
            alturaDerecha=self.right.height()+1
        if alturaIzquierda>alturaDerecha:return alturaIzquierda
        else: return alturaDerecha
    
    def balance_factor(self):
        a=0;b=0
        if self.left is not None:
            a=self.left.height()
        if self.right is not None:
            b=self.right.height()
        result=(a-b)
        
        return result
    
    def balance_factor_tree(self):
        r = self.__class__(self.balance_factor(), \
                           left=self.left.balance_factor_tree() if self.left is not None else None,
                           right=self.right.balance_factor_tree() if self.right is not None else None,
                          )
        return r