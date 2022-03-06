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

# still need to add 2 questions from the last mini quiz either on burns or drowning

def quiz(y):
    a.add(frame1, text="Question 1")
    a.add(frame2, text="Question 2")
    a.add(frame3, text="Question 3")
    a.add(frame4, text="Question 4")
    a.add(frame5, text="Question 5")
    

    Label(frame1, text="The first reflex to have should be...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame1, text="Removing contact with heat source immediately",font=("Arial",10), command=a1_right).grid(row=3, column=1)
    Button(frame1, text="Removing cloth/jewelry even if stuck to the skin",font=("Arial",10), command=a1_wrong).grid(row=3, column=2)
    Button(frame1, text="Removing cloth/jewelry near burnt area",font=("Arial",10),command=a1_right).grid(row=3, column=3)

    Label(frame2, text="Treatment for burns for all ages includes", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame2, text="Paracetamol",font=("Arial",10),command=a2_right).grid(row=3, column=1)
    Button(frame2, text="Ibuprofen",font=("Arial",10),command=a2_right).grid(row=3, column=2)
    Button(frame2, text="Aspirin",font=("Arial",10),command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="If the subject had an electrical burn", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame3, text="Call emergency medical help",font=("Arial",10),command=a3_right).grid(row=3, column=1)
    Button(frame3, text="Wait to see if they are feeling pain",font=("Arial",10),command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text="Help the subject sit down no matter how high the voltage source",font=("Arial",10),command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="If the subject had a chemical burn...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame4, text="Dry any liquid by rubbing with a napkin",font=("Arial",10),command=a4_wrong).grid(row=3, column=1)
    Button(frame4, text="Brush off any dry chemical",font=("Arial",10),command=a4_right).grid(row=3, column=2)
    Button(frame4, text="Use running water to remove the chemical without rubbing it",font=("Arial",10),command=a4_right).grid(row=3, column=3)

    Label(frame5, text="Immediately call an ambulance if the subject of the burn...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame5, text="Is going into shock (sweating, shallow breathing, cold and clammy skin...)",font=("Arial",10),command=a5_right).grid(row=3, column=1)
    Button(frame5, text="If over 60 or under 5",font=("Arial",10),command=a5_right).grid(row=3, column=2)
    Button(frame5, text="Has a medical condition/weakened immune system",font=("Arial",10),command=a5_right).grid(row=3, column=3)
    
   
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

