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

    Label(frame1, text="The first step in helping an injured person is...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame1, text="Blotting the wound dry",font=("Arial",10), command=a1_wrong).grid(row=3, column=1)
    Button(frame1, text="Putting gloves on for protection",font=("Arial",10), command=a1_right).grid(row=3, column=2)
    Button(frame1, text="Desinfecting the wound",font=("Arial",10),command=a1_wrong).grid(row=3, column=3)

    Label(frame2, text="If the subject is bleading from an injury, you should desinfect with...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame2, text="Hydrogen peroxyde",font=("Arial",10),command=a2_wrong).grid(row=3, column=1)
    Button(frame2, text="Soap and water",font=("Arial",10),command=a2_right).grid(row=3, column=2)
    Button(frame2, text="Isopropyl alcohol",font=("Arial",10),command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="Applying ice packs is useful for...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame3, text="Pain relief",font=("Arial",10),command=a3_right).grid(row=3, column=1)
    Button(frame3, text="Stopping the bleeding",font=("Arial",10),command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text="Calming the subject",font=("Arial",10),command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="If the subject is bleeding a lot but you do not have access to sterile cloth...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame4, text="Simply wait for an ambulance",font=("Arial",10),command=a4_wrong).grid(row=3, column=1)
    Button(frame4, text="Use the cloth even if dirty",font=("Arial",10),command=a4_wrong).grid(row=3, column=2)
    Button(frame4, text="Apply pressure with your hands to stop the bleeding",font=("Arial",10),command=a4_right).grid(row=3, column=3)

    Label(frame5, text="If the subject has a chest injury and is unconscious", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame5, text="Lay them down on their back",font=("Arial",10),command=a5_wrong).grid(row=3, column=1)
    Button(frame5, text="Put them in sitting position",font=("Arial",10),command=a5_wrong).grid(row=3, column=2)
    Button(frame5, text="Place them carefully on their side",font=("Arial",10),command=a5_right).grid(row=3, column=3)



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

