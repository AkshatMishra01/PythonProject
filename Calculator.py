from tkinter import *
root = Tk()
root.title('Calculator')
space = Entry(width=50 ,borderwidth=5)
space.grid(column=0,row=0,columnspan=4)

def inp(n):
   
    curr = space.get()
    space.delete(0,END)
    space.insert(0,curr + n)
   
def clear():
    space.delete(0,END)

def add():
    global op
    op = 'add'
    global first
    first = space.get()
    space.delete(0,END)


def subtract():
    global op
    op = 'sub'
    global first 
    first = space.get()
    space.delete(0,END)

def equal():
    second = space.get()
    space.delete(0,END)
    if (op == 'add'):
        space.insert(0,int(first)+int(second))
    elif (op=='sub'):
        space.insert(0,int(first)-int(second))
    elif (op=='div'):
        space.insert(0,int(first)/int(second))
    elif (op=='mul'):
        space.insert(0,int(first)*int(second))

def divide():
    global op
    op = 'div'
    global first 
    first = space.get()
    space.delete(0,END)

def mul():
    global op
    op = 'mul'
    global first 
    first = space.get()
    space.delete(0,END)


#First row
no7 = Button(text='7',padx=30,pady=20,command = lambda : inp('7')).grid(row=1,column=0)
no8 = Button(text='8',padx=30,pady=20,command = lambda : inp('8')).grid(row=1,column=1)
no9 = Button(text='9',padx=30,pady=20,command = lambda : inp('9')).grid(row=1,column=2)
div = Button(text='/',padx=30,pady=20,command = divide).grid(row=1,column=3)

#Second Row
no4 = Button(text='4',padx=30,pady=20,command = lambda : inp('4')).grid(row=2,column=0)
no5 = Button(text='5',padx=30,pady=20,command = lambda : inp('5')).grid(row=2,column=1)
no6 = Button(text='6',padx=30,pady=20,command = lambda : inp('6')).grid(row=2,column=2)
mult = Button(text='X',padx=30,pady=20,command = mul).grid(row=2,column=3)

#Third Row
no1 = Button(text='1',padx=30,pady=20,command = lambda : inp('1')).grid(row=3,column=0)
no2 = Button(text='2',padx=30,pady=20,command = lambda : inp('2')).grid(row=3,column=1)
no3 = Button(text='3',padx=30,pady=20,command = lambda : inp('3')).grid(row=3,column=2)
addi = Button(text='+',padx=30,pady=20,command = add).grid(row=3,column=3)

#Fourth Row 
dot = Button(text='.',padx=30,pady=20,command = lambda : inp('.')).grid(row=4,column=0)
no0 = Button(text='0',padx=30,pady=20,command = lambda : inp('0')).grid(row=4,column=1)
no_eq = Button(text='=',padx=30,pady=20,command = equal).grid(row=4,column=2)
sub = Button(text='-',padx=30,pady=20,command = subtract).grid(row=4,column=3)

#Fifth Row
cls = Button(text='CLS',padx=60,pady=20,command = clear).grid(row=5,column=0,columnspan=3)
root.mainloop()