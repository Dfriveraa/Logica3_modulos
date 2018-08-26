import numpy as np
def triang_store(m, init_pos=0, size=4, orientation="columns"):
    assert (m.shape[0]==m.shape[1]) 
    a=True
    for i in range (m.shape[0]-1):
        for j in range(m.shape[1]-1):
            if (i>j) and (m[i][j]!=0):
                a=False
    assert (a==True),"No es triangular"
    assert (orientation=="columns" or orientation=="rows")
    b=[init_pos]
    
    for i in range (m.shape[0]):
        for j in range(m.shape[1]-1):
            if (m[i][j]!=0):
                b+=[b[-1]+size]                    
            
    return b