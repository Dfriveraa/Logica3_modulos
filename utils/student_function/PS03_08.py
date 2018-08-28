import numpy as np
def max_per_row(m):
    max_value = 0
    row_nb = int
    
    resultado = list([])
    
    for i in m.rows.keys():
        for j in m.rows[i].keys():
            if max_value < m.rows[i][j] and m.rows[i][j] != 0:
                max_value = m.rows[i][j]
                row_nb = i
        resultado.append((row_nb, max_value))
        max_value = 0
    
    return resultado