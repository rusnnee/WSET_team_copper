# Import module
from tkinter import *
from tkinter import font
import subprocess

# Create object 
window = Tk() #Makes the window
window.config(background = "black")
window.title('Injuries')
window.geometry("1920x1080+0+24")

# Button function
def info():
    subprocess.call(['python', 'Info_injuries.py'])

def multi():
    subprocess.call(['python', 'injury_quiz.py'])

def dropdown():
    subprocess.call(['python', 'bleeding_dropdown.py'])
    
def exit_program(*args):
    window.destroy()

#Title label
title = Label( window , text = "Injuries", bg = "black", fg = 'white' )
title.config(font=('Comic Sans MS', '40'))
title.pack(pady = 60)




# Buttons
button1 = Button( window , text = "Information" , command = info, width = 30,  font=('Comic Sans MS', '20'))
button1.pack(pady = 20)

button2 = Button( window , text = "Multiple Choice Quiz" , command = multi,  width = 30,font=('Comic Sans MS', '20') )
button2.pack(pady = 20)

button3 = Button( window , text = "Select the Right Order Quiz" , command = dropdown, width = 30, font=('Comic Sans MS', '20') )
button3.pack(pady = 20)

button4 = Button(window, text = "BACK", command = exit_program, font=('Comic Sans MS', 14))
button4.place(x=10, y=10)

# Execute tkinter
window.mainloop()

