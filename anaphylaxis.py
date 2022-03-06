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

    Label(frame1, text="Click on all the symptoms of a strong allergic reaction:", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame1, text="Skin reactions (itching, hives...)",font=("Arial",10), bg="black", command=a1_right).grid(row=3, column=1)
    Button(frame1, text="Swelling of the eyes, face or throat",font=("Arial",10), bg="black", command=a1_right).grid(row=3, column=2)
    Button(frame1, text="nausea or diarrhea",font=("Arial",10), bg="black",command=a1_right).grid(row=3, column=3)

    Label(frame2, text="What can be a cause of anaphylactic shock?", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame2, text="Emotional shock",font=("Arial",10), bg="black",command=a2_wrong).grid(row=3, column=1)
    Button(frame2, text="Allergen foods",font=("Arial",10), bg="black",command=a2_right).grid(row=3, column=2)
    Button(frame2, text="High physical activity",font=("Arial",10), bg="black",command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="The first question you should ask if someone is having a strong allergic reaction", font=("Arial", 20)).grid(row=2, column=2)
    Button(frame3, text="Are you okay?",font=("Arial",10), bg="black",command=a3_wrong).grid(row=3, column=1)
    Button(frame3, text="Do you have an epinephrine autoinjector?",font=("Arial",10), bg="black",command=a3_right).grid(row=3, column=2)
    Button(frame3, text="Can you walk?",font=("Arial",10), bg="black",command=a3_wrong).grid(row=3, column=3)



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




quiz(y)
a.pack() 
root.mainloop()

