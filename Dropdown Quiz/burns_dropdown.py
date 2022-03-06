# Import module
from tkinter import *
from tkinter import font
import random
import copy

# Create object 
root = Tk()
root.geometry( "1920x1080" )
root.title('Burns Help Quiz')
root.configure(bg='black')

#Correct list
correct_list = [
    "Call 999 uf needed",
    "Cool the burn as quickly as possible with cool running water for at least 20 minutes",
    "While cooling, carefully remove jewellery and clothing, unless it's attached ot skin",
    "Cover the burn with cling film or clean dry dressing",
    "Do not apply creams, lotions or sprays to the burn",
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
title = Label( root , text = "How to help with Burns and Scalds?", bg = "black", fg = 'white' )
title.config(font=('Comic Sans MS', '30'))
title.pack(pady = 30)

# Dropdown menu options
options = copy.deepcopy(correct_list)
random.shuffle(options)

#Dropsdown menu setup

clickers = []
drops = []

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



# Button, it will check answers
button = Button( root , text = "Check" , command = show,  font=('Comic Sans MS', '15') ).pack()

# Congradulations set up
label = Label( root , text = "", bg = "black", fg = 'yellow', font=('Comic Sans MS', '25') )
label.pack()

# Execute tkinter
root.mainloop()
