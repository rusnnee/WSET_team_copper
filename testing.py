from tkinter import *

OPTIONS = (
    "egg",
    "go",
    "spam"
)

controlsMap = {}

root = Tk()

def callbackFunc(name, index, mode):
    value = root.getvar(name) #getvar: return the value of Tcl variable NAME
    widget = controlsMap[name]
    if value == 'go':
        widget.config(bg='green',fg='black',
                 activebackground='green',
                 activeforeground='black')
    else:
        widget.config(bg='SystemButtonFace',fg='SystemButtonText',
                 activebackground='SystemButtonFace',
                 activeforeground='SystemButtonText')


var1 = StringVar(root, name='var1') #give it a master and a name
var1.set(OPTIONS[0])
om1 = OptionMenu(root, var1, *OPTIONS)
om1.config(width=5)
om1.grid(row=0, column=0)
controlsMap['var1'] = om1
var1.trace_variable('w', callbackFunc)

var2 = StringVar(root, name='var2') #
var2.set(OPTIONS[0])
om2 = OptionMenu(root, var2, *OPTIONS)
om2.config(width=5)
om2.grid(row=0, column=1)
controlsMap['var2'] = om2
var2.trace_variable('w', callbackFunc)

var3 = StringVar(root, name='var3') #
var3.set(OPTIONS[0])
om3 = OptionMenu(root, var3, *OPTIONS)
om3.config(width=5)
om3.grid(row=0, column=2)
controlsMap['var3'] = om3
var3.trace_variable('w', callbackFunc)


root.mainloop()
