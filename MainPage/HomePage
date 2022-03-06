from tkinter import *
import subprocess
import time

window = Tk() #Makes the window
##window.wm_title("Copper Team WSET") #Makes the title that will appear in the top left

##rightFrame(window)
window.config(background = "black")

window.title('WSET Copper Team')
window.geometry("1920x1080+0+0")


lbl=Label(window, text="FIRST AID PLATFORM", fg='white', bg='black', font=('Comic Sans MS', 26))
lbl.place(x=550, y=61)


#Left Frame and its contents
leftFrame = Frame(window, width=500, height = 600, bg='black', highlightbackground="white", highlightcolor="white", highlightthickness=1)
leftFrame.grid(row=0, column=0, padx=30, pady=184)

leftbl=Label(window, text="Quick Actions", fg='white', bg='black', font=('Comic Sans MS', 20))
leftbl.place(x=183, y=210)

#function that when called exits program
#is here as a test currently to be replaced later
def exit_program(*args):
    window.destroy()

def emergency_program(*args):
    subprocess.call(['python', 'emergency_number.py'])

#create canvas and image
emergencyCanvas = Canvas(leftFrame, width=100, height=100, bg="#F13E3E")
#tags property allows you to bind the image in canvas to a function later
emergencyCanvas.create_rectangle(0,0, 100,100, outline='#F13E3E', fill ='#F13E3E', tags='click')
points = [50,24, 20,76, 80,76]
emergencyCanvas.create_polygon(points, width=7, outline='white', fill='#F13E3E', tags='click')
emergencyCanvas.create_oval(48,46, 52,60, outline='white', fill='white', tags='click')
emergencyCanvas.create_oval(48,62, 52,66, outline='white', fill='white', tags='click')

#binds tagged image to specified function
emergencyCanvas.tag_bind("click","<Button-1>",emergency_program)

emergencyCanvas.place(x=198, y=75)

#create canvas and image
hospitalCanvas = Canvas(leftFrame, width=100, height=100, bg="#399C5C")
#tags property allows you to bind the image in canvas to a function later
hospitalCanvas.create_rectangle(0,0, 100,100, outline='#399C5C', fill ='#399C5C', tags='click')
hospitalCanvas.create_rectangle(43,20, 58,80, outline='white', fill='white', tags='click')
hospitalCanvas.create_rectangle(20,43, 80,58, outline='white', fill='white', tags='click')
                                
#binds tagged image to specified function
hospitalCanvas.tag_bind("click","<Button-1>",exit_program)

hospitalCanvas.place(x=198, y=200)


#variable is stored in the root object
window.counter = 0

#Button functionality - recond the time and number of clicks and find bpm
time0 = 0
def clicked():
    global time0
    window.counter += 1

    if window.counter == 1:
        time0 = time.time()
        bpm = 0
    else:
        dt = time.time() - time0
        bpm = int ((window.counter/dt) *60)
        
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
    window.counter = 0
    Lspeed['text'] = 'No BPM yet'
    Lbpm.config (fg = 'white')
    Lbpm['text'] = 'Start clicking'

#VISUAL SET UP
#Title
Title = Label(leftFrame, text="BPM for CPR", bg = 'black', fg = 'white')
Title.config(font=('Comic Sans MS', 20))
Title.place(x=170, y=325)

#Click button
b = Button(leftFrame, text="Click Me", command=clicked, font=('Comic Sans MS', 14))
b.place(x=205, y=375)

#Labels
Lbpm = Label(leftFrame, text="Start clicking", bg = 'black', fg = 'white', font=('Comic Sans MS', 14))
Lbpm.place(x=185, y=425)

Lspeed = Label(leftFrame, text="No BPM yet", bg = 'black', fg = 'white', font=('Comic Sans MS', 14))
Lspeed.place(x=175, y=470)

#Restart button
Restart = Button(leftFrame, text = "Restart", command = restart, font=('Comic Sans MS', 12))
Restart.place(x=210, y=525)


#Right Frame and its contents
rightFrame = Frame(window, width=900, height = 600, bg='black', highlightbackground="white", highlightcolor="white", highlightthickness=1)
rightFrame.grid(row=0, column=1, padx=50, pady=184)


rightbl=Label(window, text="Information Hub", fg='white', bg='black', font=('Comic Sans MS', 20))
rightbl.place(x=950, y=210)

def run_program1():
    subprocess.call(['python', 'final_quiz.py'])
    #each new window will have its own function with a different name
    #run_program1, 2, 3 etc. or run_program_'button_name' etc.
def run_program2():
    subprocess.call(['python', 'burns_topic.py'])
    #each new window will have its own function with a different name
    #run_program1, 2, 3 etc. or run_program_'button_name' etc.
def run_program3():
    subprocess.call(['python', 'stroke_topic.py'])
    #each new window will have its own function with a different name
    #run_program1, 2, 3 etc. or run_program_'button_name' etc.
def run_program4():
    subprocess.call(['python', 'choking_topic.py'])
    #each new window will have its own function with a different name
    #run_program1, 2, 3 etc. or run_program_'button_name' etc.
def run_program5():
    subprocess.call(['python', 'bleeding_topic.py'])
    #each new window will have its own function with a different name
    #run_program1, 2, 3 etc. or run_program_'button_name' etc.
def run_program6():
    subprocess.call(['python', 'anaphylaxis_topic.py'])
    #each new window will have its own function with a different name
    #run_program1, 2, 3 etc. or run_program_'button_name' etc.

button1 = Button(rightFrame, text="Final Quiz", width=20, height=2, font=('Comic Sans MS', 14), command=run_program1)
button1.place(x=620, y=480)

button2 = Button(rightFrame, text="Burns", width=20, height=2, font=('Comic Sans MS', 14), command=run_program2)
button2.place(x=50, y=480)

button3 = Button(rightFrame, text="Stroke", width=20, height=2, font=('Comic Sans MS', 14), command=run_program3)
button3.place(x=620, y=280)

button4 = Button(rightFrame, text="Choking", width=20, height=2, font=('Comic Sans MS', 14), command=run_program4)
button4.place(x=50, y=280)

button5 = Button(rightFrame, text="Injury", width=20, height=2, font=('Comic Sans MS', 14), command=run_program5)
button5.place(x=620, y=80)

button6 = Button(rightFrame, text="Anaphylactic Shock", width=20, height=2, font=('Comic Sans MS', 14), command=run_program6)
button6.place(x=50, y=80)


window.mainloop() #start monitoring and updating the GUI
