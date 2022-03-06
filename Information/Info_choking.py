#Chocking


import tkinter as tk
from tkinter import *

def create_main_window():
    window = tk.Tk()
    window.title("Information on choking")
    window.geometry("1920x1080")
    window.configure(bg="black")

    Font_tuple = ("Comic Sans MS", 25, "bold")
    Font_tuple1 = ("Comic Sans MS", 15)
    Font_tuple2 = ("Comic Sans MS", 40, "bold")

    title1 = tk.Label(
        text = "Choking",
        fg = "white",
        bg="black",
        font=Font_tuple2,
        highlightthickness=4,
        highlightbackground="gray",
        width=40)
    title1.pack(ipady=10)

    main1 = tk.Label(
        text = "Choking can prevent breathing due to the blockage of food or other objects in the airway.",
        fg="white",
        bg="black",
        font=Font_tuple1, 
        justify="left")
    main1.pack()

    #Mild Choking
    subheading1 = tk.Label(
        text = "Mild Choking",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading1.pack()

    main2 = tk.Label(
        text = "Partial blocking of the airway. Encourage them to continuously cough.",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main2.pack()

    #Severe Choking
    subheading2 = tk.Label(
        text = "Severe Choking",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading2.pack()

    main3 = tk.Label(
        text = "This can be characterised by the inability to speak, breathe or swallow. Without immediate help, a person can become unconscious.\n In this case, perform back blows and the Heimlinch manouver, as described below:",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main3.pack()

    subheading3 = tk.Label(
        text = "Heimlich maneuver",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading3.pack()

    main4 = tk.Label(
        text = "1. Stand behind the person;\n2. Make a fist with one hand;\n3. Grasp the fist with the other hand; \n4. Perform between 6 and 10 abdominal thrusts until blockage is dislodged",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left",
        highlightthickness=1,
        highlightbackground="gray")
    main4.pack()

    photo1 = tk.PhotoImage(file = "choking_image.png")
    image_label = tk.Label(window, image = photo1)
    image_label.pack(ipady=10)

    main5 = tk.Label(
        text="Image taken from: istockphoto.com",
        fg = "white",
        bg="black",
        highlightthickness=4,
        highlightbackground="gray",
        width=30)
    main5.pack()

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
