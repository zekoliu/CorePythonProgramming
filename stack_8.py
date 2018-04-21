
class Stack(object):

    def __init__(self, list):
        self.list = list

    def __push__(self, newElememt):
        self.list.append(newElememt)

    def __pop__(self):
        if len(self.list) < 0:
            return None
        else:
            del self.list[-1]

    def __peek__(self):
        if len(self.list) < 0:
            return None
        else:
            return self.list[len(self.list) - 1]

    def __isempty__(self):
        if len(self.list) == 0:
            return 'this stack is empty'
        else:
            return 'this stack length is %d' % (-1)


aList = [1,2.3,4,5,6]
s = Stack(aList)
s.__push__(12)
print aList
