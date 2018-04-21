
import Tkinter
from tkMessageBox import _show

top = Tkinter.Tk()
label = Tkinter.Label(top, text = 'Hello World!')
label.pack()

enter_show = lambda : _show('button', '1111')
def change(test):
    button = test
button = '1111'
quit = Tkinter.Button(top, text = 'quit', command = top.quit, bg ='red', fg = 'white')
button1 = Tkinter.Button(top, text = '1111', command = enter_show, bg ='red', fg = 'white')
button2 = Tkinter.Button(top, text = button, command = change('kobe'), bg ='red', fg = 'white')
button3 = Tkinter.Button(top, text = '3333', command = top.quit, bg ='red', fg = 'white')
button1.pack(fill = Tkinter.X, expand = 1)
button2.pack(fill = Tkinter.X, expand = 1)
button3.pack(fill = Tkinter.X, expand = 1)
quit.pack(fill = Tkinter.X, expand=1)
Tkinter.mainloop()