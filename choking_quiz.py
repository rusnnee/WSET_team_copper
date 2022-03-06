from tkinter import *
from tkinter import ttk

y = 0
a = ttk.Notebook()

frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame(a)

def quiz(y):
    a.add(frame1, text="Question 1")
    a.add(frame2, text="Question 2")
    a.add(frame3, text="Question 3")
    a.add(frame4, text="Question 4")
    a.add(frame5, text="Question 5")

    Label(frame1, text="Click on all the symptoms of choking:", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame1, text="Difficulty or noisy breathing",font=("Arial",10), command=a1_right).grid(row=3, column=1)
    Button(frame1, text="Cough (either weak or forceful)",font=("Arial",10), command=a1_right).grid(row=3, column=2)
    Button(frame1, text="Skin, lips and nails turning blue or dusky",font=("Arial",10),command=a1_right).grid(row=3, column=3)

    Label(frame2, text="The Heimlich maneuvre consists of...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame2, text="6 to 10 abdominal thrusts",font=("Arial",10),command=a2_right).grid(row=3, column=1)
    Button(frame2, text="6 to 10 chest thrusts",font=("Arial",10),command=a2_wrong).grid(row=3, column=2)
    Button(frame2, text="1 to 3 abdomical thrusts",font=("Arial",10),command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="The 5-and-5 approach is delivered", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame3, text="If the subject can't breathe/talk forcefully",font=("Arial",10),command=a3_right).grid(row=3, column=1)
    Button(frame3, text="Whenever someone seems like they are choking",font=("Arial",10),command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text="After the subject faints",font=("Arial",10),command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="If the subject is unconscious", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame4, text="Try mouth to mouth",font=("Arial",10),command=a4_wrong).grid(row=3, column=1)
    Button(frame4, text="Try a finger sweep even if you can't see the object",font=("Arial",10),command=a4_wrong).grid(row=3, column=2)
    Button(frame4, text="Lower the subject and perform the Heimlich maneuvre",font=("Arial",10),command=a4_right).grid(row=3, column=3)

    Label(frame5, text="If the subject is an infant younger than age 1", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame5, text="Hold the infant in seating position facedown",font=("Arial",10),command=a5_right).grid(row=3, column=1)
    Button(frame5, text="Perform CPR if the infant still doesn't breathe",font=("Arial",10),command=a5_right).grid(row=3, column=2)
    Button(frame5, text="Call for emergency medical help",font=("Arial",10),command=a5_right).grid(row=3, column=3)



def a1_right():
    Label(frame1, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame1, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a1_wrong():
    Label(frame1, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame1, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a2_right():
    Label(frame2, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame2, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a2_wrong():
    Label(frame2, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame2, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a3_right():
    Label(frame3, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame3, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a3_wrong():
    Label(frame3, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame3, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a4_right():
    Label(frame4, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame4, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a4_wrong():
    Label(frame4, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame4, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a5_right():
    Label(frame5, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame5, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a5_wrong():
    Label(frame5, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame5, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)



quiz(y)
a.pack() 
root.mainloop()

