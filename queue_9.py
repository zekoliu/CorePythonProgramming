
class Queue(object):

    def __init__(self, list):
        self.list = list

    def __enqueue__(self, value):
        self.list.append(value)

    def __dequeue__(self):
        if len(self.list) == 0:
            return 'not element, do not del'
        else:
            temp = self.list[0]
            del self.list[0]
            return temp