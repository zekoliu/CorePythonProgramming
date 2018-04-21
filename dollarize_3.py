
class Dollar(object):

    def __init__(self, money):
        self.money = money

    def dollarize(self):

        str = repr(self.money)
        strList = str.split('.')
        decimel = strList[1][:2]
        ten_bit = strList[0]
        length = len(ten_bit)
        first_select = length % 3
        if first_select == 1:
            index = 1
            temp = ten_bit[:index]
            while (length - index > 0):
                temp = temp + ',' + ten_bit[index: index + 3]
                length-=3
                index += 3
            return  temp + '.' + decimel
        elif first_select == 2:
            index = 2
            temp = ten_bit[:index]
            while (length - index > 0):
                temp = temp + ',' + ten_bit[index:index+3]
                length-=3
                index += 3
            return temp + '.' + decimel
        else:
            while (length > 0):
                index = 3
                temp = ten_bit[:index]
                temp = temp + ',' + ten_bit[index: index + 3]
                length-=3
                index += 3
        return temp + '.' + decimel

    def updata(self, newMoney):
        self.money = newMoney

    def __str__(self):
        return self.dollarize()

    def __repr__(self):
        repr = str


d = Dollar(0)
print d