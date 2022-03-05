# Import module
from tkinter import *
from tkinter import font
import random
import copy

# Create object
root = Tk()
root.geometry( "1920x1080" )
root.title('Anyphalactic Shock Process quiz')
root.configure(bg='black')

#Correct list
correct_list = [
    "Call 999",
##    "Check if the person is carrying any medication",
##    "Help administer medication or, if trained, do it yourself",
##    "After injection, continue to look after the person until medical help arrives",
##    "Make sure the casualty is comfortable and can breathe as best as they can",
    ]

# Button function
def show():
    correct = 0
    for n in range(len (correct_list)):
        text = clickers[n].get()
        if (text == correct_list[n]):
            correct += 1
            drops[n].configure(state='disabled', disabledforeground = 'white')
            drops[n].config(bg="GREEN", fg="WHITE" )
            

        
    if correct == len (correct_list):
        label.config( text =  'Congratulations!' )

#Title label
title = Label( root , text = "How to help during Anaphylactic Shock?", bg = "black", fg = 'white' )
title.config(font=('Comic Sans MS', '30'))
title.pack(pady = 30)

# Dropdown menu options
options = copy.deepcopy(correct_list)
random.shuffle(options)

#Dropsdown menu setup
clickers = []
drops = []

print (len(correct_list))
for n in range (len(correct_list)):
    clicked = StringVar()
    clicked.set( "Task" + str(n+1))
    
    drop = OptionMenu( root , clicked , *options )
    drop.config (font=('Comic Sans MS', '15'), width = 80)
    drop.pack(pady = 10)

    menu = root.nametowidget(drop.menuname)
    menu.config(font=('Comic Sans MS', '12'))

    clickers.append (clicked)
    drops.append (drop)



# Button, it will check the order
button = Button( root , text = "Check" , command = show,  font=('Comic Sans MS', '15') ).pack()

# Congradulations set up
label = Label( root , text = "", bg = "black", fg = 'yellow', font=('Comic Sans MS', '25') )
label.pack()

# Execute tkinter
root.mainloop()
