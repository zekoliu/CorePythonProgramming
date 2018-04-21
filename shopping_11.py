
class User(object):
    __cart__ = Cart

    def __init__(self, cartList):
        self.cartList = cartList


class Cart(object):
    __item__ = Item

    def __init__(self, itemList):
        self.itemList = itemList


class Item(object):

    def __init__(self, item):
        self.item = item

    def __add__(self, newItem):
        self.item.append(newItem)

    def __del__(self, index):
        del self.item[index]