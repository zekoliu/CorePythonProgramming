
class MoneyFmt(object):

    def __init__(self, value = 0.0):
        self.value = float(value)

    def update(self, value = None):
        if value != None:
            self.value = value
        else:
            print 'error'
    def __repr__(self):
        return 'self.value'

    def __str__(self):
        val = ''
        val = '$' + self.value

        return val

    def __nonzero__(self):
        return int(self.value)

