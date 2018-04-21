from Tkinter import *

top = Tk()
var = IntVar()

def clickFR():
    print 'kobe'
def clickSR():
    print 'TWO'

def clickTR():
    print 'THREE'

lable = Label(top, text = 'kobe bryant', bg = 'blue', fg = 'black')
lable.pack(expand = 1)
quit = Button(top, text = 'QUIT',command = top.quit, bg = 'red', fg = 'white')
update = Button(top, text = 'update', command = clickFR(), bg = 'blue', fg = 'white')
FR = Radiobutton(top, text="One", command = clickFR(), variable = var, value=1).pack(anchor = W)
SR = Radiobutton(top, text="Two", command = clickSR(), variable = var, value=2).pack(anchor = W)
TR = Radiobutton(top, text="Three", command = clickTR(),variable = var, value=3).pack(anchor = W)
quit.pack(fill = X, expand = 1)
update.pack(fill = X, expand = 1)

mainloop()