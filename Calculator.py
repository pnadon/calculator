'''A calculator object

Philippe Nadon
December 06, 2017
'''
from tkinter import Tk, Button, Entry, END, Label, RAISED, RIDGE, Frame
from tkinter.messagebox import showinfo
from math import sqrt, e, pi, sin, cos, tan,asin,acos,atan,log


class Calc(Frame):
    'a calculator '

    def __init__(self, master):
        'calculator operator'
        Frame.__init__(self,master)

        self.pack()

        self.memory = ''    # memory
        self.expr = ''      # current expression
        self.startOfNextOperand = True # start of new operand
        self.invert = False

        # calculator button labels in a 2D list
        buttons = [
                    ['x\u00B3', 'x\u02B8', '1/x', 'INV'],
                    ['EXP', 'e', 'LOG', 'LN'],
                    ['SIN', 'COS', 'TAN', '\u03C0'],
                    ['MC', 'M+', 'M-', 'MR'],
                    ['C', '\u221A', 'x\u00B2', '+'],
                    ['7', '8', '9', '-'],
                    ['4', '5', '6', '*'],
                    ['1', '2', '3', '/'],
                    ['0', '.', '+-', '=']
                    ]

        # use Entry widget for display
        titleLabel = Label(self, text = 'Calculator')
        titleLabel.grid(row = 0, column = 0,pady = 10,columnspan = 2)

        self.entry = Entry(self, relief=RIDGE, borderwidth=3,
            width = 20, bg='cyan',
            font = ('Consolas',18))
        self.entry.grid(row=0, column=0, columnspan=5)
        self.entry.insert(0,0)

        def keyEvent(event):
            'executes click function corresponding to inputted key'
            key = event.char
            print(key)
            if key == '':
                return
            elif key == '\r':
                self.click('=')
            elif key in '0123456789-+/*=.C':
                print(key+' in')
                self.click(str(key))
        self.master.bind('<KeyPress>', keyEvent)

        # create and place buttons in appropriate row and column
        c_range = len(buttons[0])
        r_range = len(buttons)

        bcolors = ['cyan','magenta','white','gray','yellow','pink']
        for r in range(r_range):
            for c in range(c_range):

                # function cmd() is defined so that when it is
                # called without and input argument, it executes
                # self.click(buttons[r][c])
                def cmd(x=buttons[r][c]):
                    self.click(x)

                b = Button(self,
                    bg = 'white',
                    text = buttons[r][c],
                    width = 3,
                    relief=RAISED,
                    command=cmd)  #cmd() is the handler

                b.grid(row=r+1, column = c, pady = 2)     #entry is in row 0

        self.bind('<Return>', self.click('='))

    def click(self,key):
        'handler for event of pressing button labeled key'

        if key == '=':
            # evaluate the expression, including the value
            # displayed in entry and display result
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.expr = ''
                self.startOfNextOperand = True

            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')

        elif key in '+*-/':
            # add operand displayed in entry and operator key
            # to express and prespare for next operand
            self.expr += self.entry.get()
            self.expr += key
            self.startOfNextOperand = True
        # the cases when key is '\u221a', 'x\u00b2', 'C',
        # 'M+', 'M-', 'MR', 'MC' are left as an exercise

        elif key == '+-':
            # switch entry from positive to negative or vice versa
            # if there is no value in entry, do nothing
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0,'-')
            except IndexError:
                pass


        elif key == '\u221a':
            # compute and display square root of entry
            if not self.invert:
                result = sqrt(eval(self.entry.get()))
                self.entry.delete(0,END)
                self.entry.insert(END,result)
            else:
                result = eval(self.entry.get())**2
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.invert = False

        elif key == 'x\u00b2':
            # compute and displaythe square of entry
            if not self.invert:
                result = eval(self.entry.get())**2
                self.entry.delete(0,END)
                self.entry.insert(END, result)
            else:
                result = sqrt(eval(self.entry.get()))
                self.entry.delete(0,END)
                self.entry.insert(END,result)
                self.invert = False

        elif key == 'C':
            self.entry.delete(0,END)
            self.entry.insert(0,0)
            self.startOfNextOperand = True


        elif key in {'M+', 'M-'}:
            # add of subtract entry value from memory
            self.memory = str(eval(self.memory+key[1]+self.entry.get()))

        elif key == 'MR':
            # replace value in entry with value stored in memory
            self.entry.delete(0,END)
            self.entry.insert(END, self.memory)

        elif key == 'MC': #clear memory
            self.memory = ''


        elif key == 'SIN':
            if not self.invert:
                result = sin(eval(self.entry.get()))
                if result < 0:
                    result = int(result*1000)/1000
                self.entry.delete(0,END)
                self.entry.insert(END, result)
            else:
                result = asin(eval(self.entry.get()))
                if result < 0:
                    result = int(result*1000)/1000
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.invert = False

        elif key == 'COS':
            if not self.invert:
                result = cos(eval(self.entry.get()))
                if result < 0:
                    result = int(result*1000)/1000
                self.entry.delete(0,END)
                self.entry.insert(END, result)
            else:
                result = acos(eval(self.entry.get()))
                if result < 0:
                    result = int(result*1000)/1000
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.invert = False

        elif key == 'TAN':
            if not self.invert:
                result = tan(eval(self.entry.get()))
                if result < 0:
                    result = int(result*1000)/1000
                self.entry.delete(0,END)
                self.entry.insert(END, result)
            else:
                result = atan(eval(self.entry.get()))
                if result < 0:
                    result = int(result*1000)/1000
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.invert = False

        elif key == '\u03C0':
            if self.startOfNextOperand:
                self.entry.delete(0,END)
                self.entry.insert(END, pi)
            else:
                self.entry.insert(END, '*{}'.format(pi))
                self.startOfNextOperand = True


        elif key == 'LN':
            if self.invert:
                result = e**eval(self.entry.get())
                self.entry.delete(0,END)
                self.entry.insert(END, result)
            else:
                result = log(eval(self.entry.get()),e)
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.invert = False

        elif key == 'LOG':
            if self.invert:
                result = 10**eval(self.entry.get())
                self.entry.delete(0,END)
                self.entry.insert(END, result)
            else:
                result = log(eval(self.entry.get()),10)
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.invert = False


        elif key == 'x\u00B3':
            if not self.invert:
                result = eval(self.entry.get())**3
                self.entry.delete(0,END)
                self.entry.insert(END, result)
            else:
                result = eval(self.entry.get())**(1/3)
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.invert = False

        elif key == 'x\u02B8':
            self.expr += self.entry.get()
            self.expr += '**'
            self.startOfNextOperand = True

        elif key == '1/x':
            result = 1/eval(self.entry.get())
            self.entry.delete(0,END)
            self.entry.insert(END, result)
            if self.invert:
                self.invert = False


        elif key == 'INV':
            self.invert = True


        elif key == 'EXP':
            self.expr += self.entry.get()
            if not self.invert:
                self.expr += '*10**'
                self.startOfNextOperand = True
            else:
                self.expr += '*10**-'
                self.startOfNextOperand = True
                self.invert = False


        else:
            # insert digit at end of entry, or as the first
            # digit if start of next operand
            if self.startOfNextOperand:
                self.entry.delete(0,END)
                self.startOfNextOperand = False
            self.entry.insert(END, key)



class Mortgage(Frame):
    'a widget for calculating mortgage'

    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()

        titleLabel = Label(self, text = 'Mortgage Tool')
        titleLabel.grid(row = 0, column = 0,pady = 10,columnspan = 2)


        lamountLabel = Label(self, text = 'Enter loan amount in $')
        lamountLabel.grid(row = 1, column = 0,pady = 5)

        self.lamount = Entry(self)
        self.lamount.grid(row = 1, column = 1,pady = 5)

        interestLabel = Label(self, text = 'Enter interest in %')
        interestLabel.grid(row = 2, column = 0,pady = 5)

        self.interest = Entry(self)
        self.interest.grid(row = 2, column = 1,pady = 5)

        ltermLabel = Label(self, text = 'Enter months required to pay loan')
        ltermLabel.grid(row = 3, column = 0,pady = 5)

        self.lterm = Entry(self)
        self.lterm.grid(row = 3, column = 1,pady = 5)

        def compute():
            'displays mortgage using the inputted data'
            try:
                c = float(self.interest.get())/1200
                a = float(self.lamount.get())
                t = float(self.lterm.get())
            except:
                showinfo(message = 'Error')
                return
            result = (a*c*(1+c)**t)/(((1+c)**t)-1)
            showinfo(message = 'Your monthly mortgage is at {}$'.format(result))

        button = Button(self, text = 'Compute',command = compute)
        button.grid(row = 4, column = 0, columnspan = 2)

root = Tk()
mycalc = Calc(root)
mycalc.master.title("Python Calculator")
mortgage = Mortgage(root)

root.mainloop()
