#Injuries

from curses import window
from logging import root
import tkinter as tk
from tkinter import *
from turtle import color

def create_main_window():
    window = tk.Tk()
    window.title("Information on general injuries")
    window.geometry("1920x1080")
    window.configure(bg="black")

    Font_tuple = ("Comic Sans MS", 25, "bold")
    Font_tuple1 = ("Comic Sans MS", 15)
    Font_tuple2 = ("Comic Sans MS", 40, "bold")

    title1 = tk.Label(
        text = "General injuries",
        fg = "white",
        bg="black",
        font=Font_tuple2,
        highlightthickness=4,
        highlightbackground="gray",
        width=40)
    title1.pack(ipady=10)

    subheading1 = tk.Label(
            text = "CPR",
            fg = "white",
            bg="black",
            font = Font_tuple,
            justify="left")
    subheading1.pack() 

    main1 = tk.Label(
        text = "If a person is unconscious but breathing, they should be put in the recovery position. \nEnsure their breathing is not obstructed, as shown in the first image below. \nIf a person is unconscious and not breathing, CPR should be done, as described on the second image below.",
        fg="white",
        bg="black",
        font=Font_tuple1, 
        justify="left")
    main1.pack()

    photo1 = tk.PhotoImage(file = "recovery_image.png")
    image_label = tk.Label(window, image = photo1)
    image_label.pack(ipady=10)

    main2 = tk.Label(
        text="Image taken from: istockphoto.com",
        fg = "white",
        bg="black",
        highlightthickness=4,
        highlightbackground="gray",
        width=30)
    main2.pack()

    photo2 = tk.PhotoImage(file = "cpr_image.png")
    image_label = tk.Label(window, image = photo2)
    image_label.pack(ipady=10)

    main3 = tk.Label(
        text="Image taken from: healthline.com",
        fg = "white",
        bg="black",
        highlightthickness=4,
        highlightbackground="gray",
        width=30)
    main3.pack()

    #Cuts and bleedings
    subheading2 = tk.Label(
        text = "Cuts and bleedings",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading2.pack()

    main4 = tk.Label(
        text = "Under the circumstance someone is breathing heavily: \n1. Apply pressure to the side of the wound, ensuring there is no object embedded inside until bleeding stops, \n2. Firmly bandage the wound with clean dressing. \nFor minor cuts, run under cold water and put on a plaster to prevent infection of the wound.",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main4.pack()

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
