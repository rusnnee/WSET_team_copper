from tkinter import *
import time

root = Tk()
root.geometry( "1920x1080" )
root.title('BMP for CPR counter')
root.configure(bg='black')

#variable is stored in the root object
root.counter = 0

#Button functionality - recond the time and number of clicks and find bpm
time0 = 0
def clicked():
    global time0
    root.counter += 1

    if root.counter == 1:
        time0 = time.time()
        bpm = 0
    else:
        dt = time.time() - time0
        bpm = int ((root.counter/dt) *60)
        
    #Updating text
    Lbpm['text'] = 'Your BPM is ' + str(bpm)
    if bpm < 100:
        Lbpm.config (fg = 'red')
        Lspeed['text'] = 'Your CPR is too slow'
    elif bpm <120:
        Lbpm.config (fg = 'green')
        Lspeed['text'] = 'Your CPR is the correct speed'
    else:
        Lbpm.config (fg = 'red')
        Lspeed['text'] = 'Your CPR is too fast'

#Restart button functionality
def restart():
    root.counter = 0
    Lspeed['text'] = 'No BPM yet'
    Lbpm.config (fg = 'white')
    Lbpm['text'] = 'Start clicking'

#VISUAL SET UP
#Title
Title = Label(root, text="BPM for CPR", bg = 'black', fg = 'white')
Title.config(font=('Comic Sans MS', '30'))
Title.pack( pady = 40)

#Click button
b = Button(root, text="Click Me", command=clicked, font=('Comic Sans MS', '20'))
b.pack()

#Labels
Lbpm = Label(root, text="Start clicking", bg = 'black', fg = 'white', font=('Comic Sans MS', '20'))
Lbpm.pack(pady = 10)

Lspeed = Label(root, text="No BPM yet", bg = 'black', fg = 'white', font=('Comic Sans MS', '20'))
Lspeed.pack(pady = 10)

#Restart button
Restart = Button(root, text = "Restart", command = restart, font=('Comic Sans MS', '15'))
Restart.pack(pady = 20)
root.mainloop()
