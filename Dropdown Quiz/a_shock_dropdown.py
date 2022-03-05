# Import module
from tkinter import *
import random
import copy

# Create object
root = Tk()

# Adjust size
root.geometry( "1920x1080" )

#Correct list
correct_list = [
    "Call 999",
    "Check if the person is carrying any medication",
    "Help administer medication or, if trained, do it yourself",
    "After injection, continue to look after the person until medical help arrives",
    "Make sure the casualty is comfortable and can breathe as best as they can",
    ]

# Button function
def show():
    correct = 0
    for n in range(len (correct_list)):
        text = clickers[n].get()
        if (text == correct_list[n]):
            correct += 1
            drops[n].config(bg="GREEN", fg="WHITE")
        
    label.config( text =  'The number of correct answers is ' + str(correct) )

# Dropdown menu options
options = copy.deepcopy(correct_list)
random.shuffle(options)

#MY OWN CODE
clickers = []
drops = []

print (len(correct_list))
for n in range (len(correct_list)):
    clicked = StringVar()
    clicked.set( "Task" + str(n+1))
    
    drop = OptionMenu( root , clicked , *options )
    drop.pack()
    clickers.append (clicked)
    drops.append (drop)



# Create button, it will change label text
button = Button( root , text = "Check" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()
