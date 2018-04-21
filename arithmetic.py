
def arithmetic(fisrstnum, operator, secondnum):
    if (operator == '+'):
        return fisrstnum + secondnum
    elif (operator == '-'):
        return fisrstnum - secondnum
    elif (operator == "*"):
        return fisrstnum * secondnum
    elif (operator == '/'):
        return fisrstnum / secondnum

print arithmetic(1, '+', 9)