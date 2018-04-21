
import time

class Data(object):

    def __init__(self, data = time.localtime()):
        self.data = data

    def __updata__(self, newData):
        self.data = newData

    def __display__(self, displaytype):
        day = self.timeValue.tm_mday
        if day <= 9:
            day2 = '0' + str(day)
        else:
            day2 = str(day)

        months = self.timeValue.tm_mon
        if months <= 9:
            months2 = '0' + str(months)
        else:
            months2 = str(months)

        year = self.timeValue.tm_year
        year2 = str(year)[2:]
        year4 = str(year)

        timeStringSplit = self.timeString.split()

        if displaytype == 'MDY':
            return months2 + '/' + day2 + '/' + year2
        elif displaytype == 'MDYY':
            return months2 + '/' + day2 + '/' + year4
        elif displaytype == 'DMYY':
            return day2 + '/' + months2 + '/' + year2
        elif displaytype == 'DMY':
            return day2 + '/' + months2 + '/' + year4
        elif displaytype == 'MODYY':
            return timeStringSplit[0] + ' ' + timeStringSplit[2] + ', ' + timeStringSplit[4]
        else:
            return self.timeString


