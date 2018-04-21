
import os

class CapOpen(object):
    def __init__(self, fn, mode = 'r', buf = -1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def writelines(self, lines, enter = False):
        for eachLine in lines:
            if enter:
                eachLine +=  os.linesep
            self.file.write(lines.upper())