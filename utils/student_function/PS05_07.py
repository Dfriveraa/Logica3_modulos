from IPython.display import Math

class VarTerm():
    def __init__(self, coef, var, exp=1):
        assert (isinstance(coef, float) or isinstance(coef,int)) and \
                isinstance(exp, int) and isinstance(var, str) and len(var)==1
        self.coef = coef
        self.var  = var
        self.exp  = exp
        
    def get_math_representation(self):
        s = ("%s"%str(self.coef) if self.coef!=1 else "") +\
            (" %s"%self.var if self.exp==1 else (" %s^%d"%(self.var, self.exp) if self.exp!=0 else "")) 
        return s
    
    def __repr__(self):
        return self.get_math_representation() 
        
    def evaluate(self, vals):
        var=vals[self.var]
        return self.coef*(var**self.exp)