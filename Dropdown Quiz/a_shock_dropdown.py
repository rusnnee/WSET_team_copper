# Import module
from tkinter import *
import random

# Create object
root = Tk()

# Adjust size
root.geometry( "1920x1080" )

#Correct list
correct_list = [
    "Call 999",
    "Check if the person is carrying any medication",
    "Help administer medication or, if trained, do it yourself",
    "task 4",
    "tsk 5",
    "6",
    "7"]

# Button function
def show():
    correct = 0
    for n in range(7):
        text = clickers[n].get()
        if (text == correct_list[n]):
            correct += 1
            drops[n].config(bg="GREEN", fg="WHITE")
        
    label.config( text =  'The number of correct answers is ' + str(correct) )

# Dropdown menu options
options =[
	"Call 999",
    "Check if the person is carrying any medication",
    "Help administer medication or, if trained, do it yourself",
    "task 4",
    "tsk 5",
    "6",
    "7"
]
random.shuffle(options)


#MY OWN CODE
clickers = []
drops = []
random.shuffle(options)

for n in range (7):
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
