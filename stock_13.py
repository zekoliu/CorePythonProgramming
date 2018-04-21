
class Stock(object):

    def __init__(self, allStock, company, stockCode, purchaseDate, price, shareNumbers):
        self.allStock = allStock
        self.company = company
        self.stockCode = stockCode
        self.purnchaseDate = purchaseDate
        self.price = price
        self.shareNumbers = shareNumbers

    def __addStock__(self, newStock):
        return self.allStock.append(newStock)

    def __delStock__(self, sellStock):
        return self.allStock.remove(sellStock)
