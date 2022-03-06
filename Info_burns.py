#Burns

from curses import window
from logging import root
import tkinter as tk
from tkinter import *
from turtle import color

def create_main_window():
    window = tk.Tk()
    window.title("Information on burns")
    window.geometry("1920x1080")
    window.configure(bg="black")

    scrollbar1 = Scrollbar(window, orient="vertical", bg="black")
    scrollbar1.pack(side=RIGHT, fill=Y)

    Font_tuple = ("Comic Sans MS", 25, "bold")
    Font_tuple1 = ("Comic Sans MS", 15)
    Font_tuple2 = ("Comic Sans MS", 40, "bold")

    title1 = tk.Label(
        text = "Burns and Scalds",
        fg = "white",
        bg="black",
        font=Font_tuple2,
        highlightthickness=4,
        highlightbackground="gray",
        width=40)
    title1.pack(ipady=10)

    main1 = tk.Label(
        text = "Dry heat causes burns, whilst scalds are caused by something wet. They are both damages to skin due to heat.",
        fg="white",
        bg="black",
        font=Font_tuple1, 
        justify="left")
    main1.pack()

    #Treating burns
    subheading1 = tk.Label(
        text = "How to treat burns and scalds",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading1.pack()

    main2 = tk.Label(
        text = "1. Immediately move away from the heat source and cool the burn; \n2.Remove any clothing around the burnt area; \n3.Make sure the person keeps warm; \n4. Cover the burn.",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main2.pack()

    #Serious burns
    subheading2 = tk.Label(
        text = "Serious burns",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading2.pack()

    main3 = tk.Label(
        text = "These require medical attention. Some examples of severe burns are: \n- Chemical and electrical burns; \n- Large or deep burns; \n- Burns that cause white or charred skin; \n- Burns on the face, hands, arms, feet, legs or genitals that cause blisters.",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main3.pack()

    #Types of burns
    subheading3 = tk.Label(
        text = "Types of burns",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading3.pack()

    main4 = tk.Label(
        text = "Burns are assessed based on how the skin layers were affected. The image below describes the types of burns:",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main4.pack()

    photo1 = tk.PhotoImage(file = "burns_image.png")
    image_label = tk.Label(window, image = photo1)
    image_label.pack(ipady=10)

    main5 = tk.Label(
        text="Image taken from: www.stjohnvic.com.au",
        fg = "white",
        bg="black",
        highlightthickness=4,
        highlightbackground="gray",
        width=30)
    main5.pack()

    window.mainloop()

if __name__ == "__main__":
    create_main_window()