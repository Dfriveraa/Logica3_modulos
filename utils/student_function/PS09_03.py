def recover_path(path, cost, target):
     camino=[]
     d={}
     default=None
     coste = cost[(target)]
     camino.append(target)
     for i in range(len(path)-1):
         camino.append(path.setdefault((target),default))
         target=path[target]
     camino=list([d.setdefault(x,x) for x in camino if x not in d])
     camino.remove(None)
     camino.reverse()
     return camino, coste