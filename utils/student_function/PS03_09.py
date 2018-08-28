import numpy as np
def max_per_col(m):
    max_value = 0
    col_nb = int
    resultado = list([])
    
    for i in range(m.shape[1]):
        col_nb = i
        for j in range(m.shape[0]):
            if j in m.rows.keys():
                if i in m.rows[j].keys():
                    if max_value < m.rows[j][i] and m.rows[j][i] != 0:
                        max_value = m.rows[j][i]
        if max_value != 0:
            resultado.append((col_nb, max_value))
        max_value = 0
        
    return resultado