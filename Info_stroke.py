#stroke


import tkinter as tk
from tkinter import *

def create_main_window():
    window = tk.Tk()
    window.title("Information on stroke")
    window.geometry("1920x1080")
    window.configure(bg="black")

    Font_tuple = ("Comic Sans MS", 25, "bold")
    Font_tuple1 = ("Comic Sans MS", 15)
    Font_tuple2 = ("Comic Sans MS", 40, "bold")

    title1 = tk.Label(
        text = "Stroke",
        fg = "white",
        bg="black",
        font=Font_tuple2,
        highlightthickness=4,
        highlightbackground="gray",
        width=40)
    title1.pack(ipady=10)

    main1 = tk.Label(
        text = "Happens as a result of blood supply being cut off to a part of the brain. \nThe consequences of this medical condition can be life-threatening, and therefore immediate medical attention is required. \n It is imperative that a person receives treatment as soon as possible.",
        fg="white",
        bg="black",
        font=Font_tuple1, 
        justify="left")
    main1.pack()

    #Detecting a stroke
    subheading1 = tk.Label(
        text = "Detecting a stroke",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading1.pack()

    main2 = tk.Label(
        text = "Remember FAST: \nFACE = may become drooped onto one side and unable to smile, \nARMS = may not be able to life, \nSPEECH = may become slurred or incoherent, \nTIME = call 999.",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main2.pack()

    #Treatments
    subheading2 = tk.Label(
        text = "Treatment",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading2.pack()

    main3 = tk.Label(
        text = "Call 999 if you suspect someone is having a stroke",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main3.pack(ipady=10)

    photo1 = tk.PhotoImage(file = "stroke_image.png")
    image_label = tk.Label(window, image = photo1)
    image_label.pack(ipady=20)

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
