
class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        self.min = min

    def __str__(self):
        'Time60 - string representation'
        return '%f:%f' % (self.hr, self.min)

    def __add__(self, other):
        'Time60 -overloading the addition operator'
        return self.__class__(float(self.hr) + float(other.hr), float(self.hr) + float(self.min))

    def __iadd__(self, other):
        hr_temp = float(self.hr)
        min_temp = float(self.min)
        hr_temp += float(other.hr)
        min_temp += float(other.min)
        return self