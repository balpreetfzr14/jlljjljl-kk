from tkinter import*
from datetime import date
window = Tk()
window.title('hello')
window.geometry('400x300')
lab  = Label(text = 'hey there',fg = "white", bg = "#465454",height = 2, width=  300)
nlab = Label(text = "full name",bg  = "#64b475")
nent = Entry()
def display():
    name = nent.get()
    global message
    message = 'welcome to the application \n todays date is : '
    greet = "hello"+name+'\n'
    txb.insert(END,greet)
    txb.insert(END,message)
    txb.insert(END,date.today)
txb = Text(height = 3,bg = '#01fae9', fg = '#050505')
btn = Button(text = 'begin',command = display,height = 1,bg = '#03cf88', fg = '#565555')
lab.pack()
nlab.pack()
nent.pack()
btn.pack()
txb.pack()
window.mainloop()

