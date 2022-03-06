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

    Label(frame1, text="Click on all the symptoms of a stroke:", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame1, text="Sudden blurry vision",font=("Arial",10), command=a1_right).grid(row=3, column=1)
    Button(frame1, text="Numbness, especially on one member",font=("Arial",10), command=a1_right).grid(row=3, column=2)
    Button(frame1, text="Sudden confusion or trouble speaking clearly",font=("Arial",10),command=a1_right).grid(row=3, column=3)

    Label(frame2, text="F.A.S.T stands for...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame2, text="Funny Appearance Sound Tone",font=("Arial",10),command=a2_wrong).grid(row=3, column=1)
    Button(frame2, text="Face Arms Speach Time",font=("Arial",10),command=a2_right).grid(row=3, column=2)
    Button(frame2, text="Feet Abdomen Stomach Tongue",font=("Arial",10),command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="The first reflex you should have is...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame3, text="To call an ambulance",font=("Arial",10),command=a3_right).grid(row=3, column=1)
    Button(frame3, text="To perform CPR",font=("Arial",10),command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text="To bring water to the subject",font=("Arial",10),command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="Click on everything you should NOT do:", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame4, text="Feed the subject",font=("Arial",10),command=a4_right).grid(row=3, column=1)
    Button(frame4, text="Let the subject fall asleep",font=("Arial",10),command=a4_right).grid(row=3, column=2)
    Button(frame4, text="Give the subject medication",font=("Arial",10),command=a4_right).grid(row=3, column=3)

    Label(frame5, text="If the symptoms vanish after a few minutes...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame5, text="The subject is safe",font=("Arial",10),command=a5_wrong).grid(row=3, column=1)
    Button(frame5, text="The subject should take some rest",font=("Arial",10),command=a5_wrong).grid(row=3, column=2)
    Button(frame5, text="Still call for medical help",font=("Arial",10),command=a5_right).grid(row=3, column=3)



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

