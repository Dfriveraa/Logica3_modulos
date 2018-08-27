def add_to_dict(d, key1, key2, val):
    if d.get(key1)==None:
        d[key1]={}
    d[key1][key2]=val  
    return d