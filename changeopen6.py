
def safe_open(filename, opentype):
    try:
        f = open(filename, opentype)
        return f
    except IOError, e:
        print e
        return None

if __name__ == '__main__':
    safe_open('/home/jenenliu/Desktop/kobe.txt', 'w')
