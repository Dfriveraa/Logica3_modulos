def PriorityQueue():
    class _PriorityQueue:
        def __init__(self):
            self.elements = []
            self.order=[]

        def empty(self):
            return False if(self.elements) else True

        def put(self, item, priority):
            while len(self.elements)<=priority:
                self.elements.append(None)
            self.elements.insert(priority,item)

        def get(self):
            if self.empty():return None
            for i in self.elements:
                if i is not None:
                    a=i
                    self.elements.remove(i)
                    return a
        

    return _PriorityQueue()
    