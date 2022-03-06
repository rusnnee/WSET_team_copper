from tkinter import *
from tkinter import ttk

y = 0
a = ttk.Notebook()

frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)
frame6 = ttk.Frame(a)
frame7 = ttk.Frame(a)
frame8 = ttk.Frame(a)
frame9 = ttk.Frame(a)
frame10 = ttk.Frame(a)

root = ttk.Frame(a)

# still need to add 2 questions from the last mini quiz either on burns or drowning

def quiz(y):
    a.add(frame1, text="Question 1")
    a.add(frame2, text="Question 2")
    a.add(frame3, text="Question 3")
    a.add(frame4, text="Question 4")
    a.add(frame5, text="Question 5")
    a.add(frame6, text="Question 6")
    a.add(frame7, text="Question 7")
    a.add(frame8, text="Question 8")
    a.add(frame9, text="Question 9")
    a.add(frame10, text="Question 10")

    Label(frame1, text="The first step in helping an injured person is...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame1, text="Blotting the wound dry",font=("Arial",10), command=a1_wrong).grid(row=3, column=1)
    Button(frame1, text="Putting gloves on for protection",font=("Arial",10), command=a1_right).grid(row=3, column=2)
    Button(frame1, text="Desinfecting the wound",font=("Arial",10),command=a1_wrong).grid(row=3, column=3)

    Label(frame2, text="F.A.S.T stands for...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame2, text="Funny Appearance Sound Tone",font=("Arial",10),command=a2_wrong).grid(row=3, column=1)
    Button(frame2, text="Face Arms Speach Time",font=("Arial",10),command=a2_right).grid(row=3, column=2)
    Button(frame2, text="Feet Abdomen Stomach Tongue",font=("Arial",10),command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="If the subject is bleading from an injury, you should desindect with...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame3, text="Hydrogen peroxyde",font=("Arial",10),command=a3_wrong).grid(row=3, column=1)
    Button(frame3, text="Soap and water",font=("Arial",10),command=a3_right).grid(row=3, column=2)
    Button(frame3, text="Isopropyl alcohol",font=("Arial",10),command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="The first question you should ask if someone is having a strong allergic reaction is...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame4, text="Are you okay?",font=("Arial",10),command=a4_wrong).grid(row=3, column=1)
    Button(frame4, text="Do you have an epinephrine autoinjector?",font=("Arial",10),command=a4_right).grid(row=3, column=2)
    Button(frame4, text="Can you walk?",font=("Arial",10),command=a4_wrong).grid(row=3, column=3)

    Label(frame5, text="The Heimlich maneuvre consists of...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame5, text="6 to 10 abdominal thrusts",font=("Arial",10),command=a5_right).grid(row=3, column=1)
    Button(frame5, text="6 to 10 chest thrusts",font=("Arial",10),command=a5_wrong).grid(row=3, column=2)
    Button(frame5, text="1 to 3 abdomical thrusts",font=("Arial",10),command=a5_wrong).grid(row=3, column=3)
    
    Label(frame6, text="Click on all the symptoms of a stroke:", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame6, text="Sudden blurry vision",font=("Arial",10), command=a6_right).grid(row=3, column=1)
    Button(frame6, text="Numbness, especially on one member",font=("Arial",10), command=a6_right).grid(row=3, column=2)
    Button(frame6, text="Sudden confusion or trouble speaking clearly",font=("Arial",10),command=a6_right).grid(row=3, column=3)

    Label(frame7, text="Click on all the symptoms of a strong allergic reaction:", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame7, text="Skin reactions (itching, hives...)",font=("Arial",10), command=a7_right).grid(row=3, column=1)
    Button(frame7, text="Swelling of the eyes, face or throat",font=("Arial",10), command=a7_right).grid(row=3, column=2)
    Button(frame7, text="nausea or diarrhea",font=("Arial",10),command=a7_right).grid(row=3, column=3)

    Label(frame8, text="If an infant younger than age 1 is choking...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame8, text="Hold the infant in seating position facedown",font=("Arial",10),command=a8_right).grid(row=3, column=1)
    Button(frame8, text="Perform CPR if the infant still doesn't breathe",font=("Arial",10),command=a8_right).grid(row=3, column=2)
    Button(frame8, text="Call for emergency medical help",font=("Arial",10),command=a8_right).grid(row=3, column=3)

    Label(frame9, text="If the subject had an electrical burn", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame9, text="Call emergency medical help",font=("Arial",10),command=a9_right).grid(row=3, column=1)
    Button(frame9, text="Wait to see if they are feeling pain",font=("Arial",10),command=a9_wrong).grid(row=3, column=2)
    Button(frame9, text="Help the subject sit down no matter how high the voltage source",font=("Arial",10),command=a9_wrong).grid(row=3, column=3)

    Label(frame10, text="Immediately call an ambulance if the subject of the burn...", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame10, text="Is going into shock (sweating, shallow breathing, cold and clammy skin...)",font=("Arial",10),command=a10_right).grid(row=3, column=1)
    Button(frame10, text="If over 60 or under 5",font=("Arial",10),command=a10_right).grid(row=3, column=2)
    Button(frame10, text="Has a medical condition/weakened immune system",font=("Arial",10),command=a10_right).grid(row=3, column=3)

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

def a6_right():
    Label(frame6, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame6, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a6_wrong():
    Label(frame6, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame6, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a7_right():
    Label(frame7, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame7, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a7_wrong():
    Label(frame7, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame7, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a8_right():
    Label(frame8, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame8, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a8_wrong():
    Label(frame8, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame8, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a9_right():
    Label(frame9, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame9, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a9_wrong():
    Label(frame9, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame9, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)

def a10_right():
    Label(frame10, text="Correct!",font=("Arial",20),bg="green",fg="white").grid(row=1,column=2)
    Label(frame10, text="Score:+1", font=("Arial",20),bg="green",fg="white").grid(row=1,column=3)
def a10_wrong():
    Label(frame10, text="Incorrect!",font=("Arial",20),bg="red",fg="white").grid(row=1,column=2)
    Label(frame10, text="Score:0", font=("Arial",20),bg="red",fg="white").grid(row=1,column=3)


quiz(y)
a.pack() 
root.mainloop()

