import numpy as np
def diag_store(a, init_pos=0, size=4):
    assert (a.shape[0]==a.shape[1]) and (np.array_equal(a,np.diag(np.diag(a))))
    b=[init_pos]
    for i in range(a.shape[0]-1):
        for j in range(a.shape[0]-1):
            if i==j:
                b+=[b[i]+size]
    return b