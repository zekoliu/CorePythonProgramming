
class Shell(object):

    def __init__(self, ls, more, cat, cp, mv, rm):
        self.ls = ls
        self.more = more
        self.cat = cat
        self.cp = cp
        self.mv = mv
        self.rm = rm

    def __ls__(self):
        return dir('.')

    def __more__(self, filename):
        return  filename.more()

    def __cat__(self, tp):
        return type(tp)

    def __cp__(self, newFilename):
        return newFilename.copy()

    def __mv__(self):
        pass

    def __rm__(self, filename):
        del filename
