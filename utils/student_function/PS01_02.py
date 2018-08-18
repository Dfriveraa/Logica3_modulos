def getremove_last(l):
    assert len(l)==0,"error"
    val=l[-1]
    rest_list=l[:len(l)-1]
    return val, rest_list