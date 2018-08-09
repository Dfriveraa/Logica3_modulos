import numpy as np
import random
def fill(t, n):
    a=0
    while a<n:
        t.put(random.randrange(10))
        a=a+1
    return t