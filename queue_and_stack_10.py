
class QueueAndStack(object):

    def __init__(self, list):
        self.list = list

    def __shift__(self):
        temp =  self.list[0]
        del self.list[0]
        return temp

    def __unshift__(self, newElememt):
        return self.list.insert(0, newElememt)

    def __push__(self, newElememt):
        return self.list.append(newElememt)

    def __pop__(self):
        temp = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]
        return temp

list = [1,2,3,4,5,6]
q = QueueAndStack(list)
print q.__shift__()