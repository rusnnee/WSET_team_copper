# Import module
from tkinter import *
from tkinter import font
import subprocess

# Create object 
window = Tk() #Makes the window
window.config(background = "black")
window.title('Choking')
window.geometry("1920x1080+0+24")

# Button function
def info():
    subprocess.call(['python', 'burns_topic.py'])

def multi():
    subprocess.call(['python', 'burns_topic.py'])

def dropdown():
    subprocess.call(['python', 'burns_topic.py'])

#Title label
title = Label( window , text = "Burns and Scalds", bg = "black", fg = 'white' )
title.config(font=('Comic Sans MS', '40'))
title.pack(pady = 60)

# Buttons
button1 = Button( window , text = "Information" , command = info, width = 30,  font=('Comic Sans MS', '20'))
button1.pack(pady = 20)

button2 = Button( window , text = "Multiple Choice Quiz" , command = multi,  width = 30,font=('Comic Sans MS', '20') )
button2.pack(pady = 20)

button3 = Button( window , text = "Select the Right Order Quiz" , command = dropdown, width = 30, font=('Comic Sans MS', '20') )
button3.pack(pady = 20)
# Execute tkinter
window.mainloop()
