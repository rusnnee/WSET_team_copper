# Import module
from tkinter import *
import random

# Create object
root = Tk()

# Adjust size
root.geometry( "1920x1080" )

# Change the label text
def show():
	label.config( text = clicked.get() )

# Dropdown menu options
options_list =[
	"Call 999",
	"Check if the person is carrying any medication",
	"Help administer medication or, if trained, do it yourself",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]
random.shuffle(options_list)
options = options_list

# datatype of menu text
clicked1 = StringVar()
clicked2 = StringVar()

# initial menu text
clicked1.set( "Task 1" )
clicked2.set( "Task 2" )

# Create Dropdown menu
drop1 = OptionMenu( root , clicked1 , *options )
drop1.pack()

drop2 = OptionMenu( root , clicked2 , *options )
drop2.pack()

# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()
