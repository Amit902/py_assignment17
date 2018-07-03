#Q1 Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

from tkinter import *

def show():
    print("hello world!")
    print("hello python!")

root= Tk()
b1=Button(root,text="hello world !",width=20,fg='black',font='white',bg='light pink')
b1.pack()

b2=Button(root,text="hello python !",width=20,fg='black',font='white',bg='light pink')
b2.pack()

b3=Button(root,text="exit",width=10,fg='white',bg="blue",command=exit)
b3.pack()
root.mainloop()
print("\n")


#Q2. Write a python program to in the same interface as above and create a action
#    when the button is click it will display some text.

from tkinter import *

def show():
    print(" amit is also a nice guy for coding in python display some text in the cintext of python")


root= Tk()
b=Button(root,text="click here",width=20,fg='white',font='white',bg='green',command=show)
b.pack()
root.mainloop()
print("\n")


#Q3. Create a frame using tkinter with any label text and two buttons.
#    One to exit and other to change the label to some other text.

from tkinter import *

def display():
    var.set("Hello python something going intresting in GUI")

def terminate():
    exit(0)

root = Tk()

var=StringVar()

root.geometry("300x300")

b1 = Button(root,text="click",width=50,bg='light blue',font='black',command=display)
b1.pack()

b2 = Button(root,text="exit",width=50,bg='light blue',font='black',command=terminate)
b2.pack()

var.set("This is going something funny study")
label=Label(textvariable=var)
label.pack()
root.mainloop()
print("\n")


#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.

from tkinter import *

def show():
    print(entry.get())

root=Tk()

entry=Entry(root,width=50,bg='light blue',font='black')
entry.pack()
a=Button(root,text='click here',width=20,bg='light green',command=show)
a.pack()
b=Button(root,text="exit",width=10,fg='white',bg="blue",command=exit)
b.pack()
root.mainloop()
