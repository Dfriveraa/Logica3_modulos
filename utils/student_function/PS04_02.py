import numpy as np
def triang_store(m, init_pos=0, size=4, orientation="columns"):
    assert m.shape[0] == m.shape[1]
    assert np.allclose(m, np.triu(m)) == True
    
    if orientation != "columns" and orientation != "rows":
        raise AssertionError()
        
    diagonal = np.diagonal(m)
    
    triang_storage_size = ((diagonal.size*diagonal.size)-diagonal.size)/2 + diagonal.size
    diagonal_storage = np.zeros(triang_storage_size)
    diagonal_storage[0] = init_pos
    
    i=1

    while i < triang_storage_size:
        diagonal_storage[i] = diagonal_storage[i-1] + size
        i+=1

    
    return diagonal_storage