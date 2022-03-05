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

    label.config( text = clicked.get() )
    
##    correct = 0
##    for n in range(7):
##        text = clickers(n).get()
##        if (text == correct_list(n)):
##            print ("correct")
##            correct += 1
##        else:
##            print ("incorrect")
##        
##    label.config( text =  '' )

# Dropdown menu options
options =[
	"Call 999",
	"Check if the person is carrying any medication",
	"Help administer medication or, if trained, do it yourself",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]
random.shuffle(options)


#MY OWN CODE
clickers = []
drops = []
for n in range (7):
    random.shuffle(options)
    clicked = StringVar()
    clicked.set( "Task" + str(n+1))
    drop = OptionMenu( root , clicked , *options )
    drop.pack()
    
    clickers.append (clicked)
    drops.append (drop)

# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()
