
from Tkinter import *

def fork(txt):
    label = Label(top, text = txt)
    label.pack()

top = Tk()
entry = Entry(top)
entry.pack()
button = Button(top, text = 'Enter', command = fork(entry.get()), fg = 'white', bg = 'red')
button.pack()
print entry.get()
mainloop()
