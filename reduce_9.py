
def average(list):
    total = reduce((lambda  x,y:x+y), list)
    return (float(total) / len(list))

list = [2,2,3,3]
print average(list)