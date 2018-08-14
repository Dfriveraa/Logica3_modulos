import numpy as np
def add_lists(a,b):
    while (len(a)<len(b)):
        a=a+[0]
    while(len(a)>len(b)):
        b=b+[0]
    na=np.array(a)
    nb=np.array(b)
    
    return list(na+nb)