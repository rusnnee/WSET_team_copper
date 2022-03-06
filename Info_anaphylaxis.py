#Anaphylaxis


import tkinter as tk
from tkinter import *

def create_main_window():
    window = tk.Tk()
    window.title("Information on anaphylaxis")
    window.geometry("1920x1080")
    window.configure(bg="black")

    Font_tuple = ("Comic Sans MS", 25, "bold")
    Font_tuple1 = ("Comic Sans MS", 15)
    Font_tuple2 = ("Comic Sans MS", 40, "bold")

    title1 = tk.Label(
        text = "Anaphylaxis",
        fg = "white",
        bg="black",
        font=Font_tuple2,
        highlightthickness=4,
        highlightbackground="gray",
        width=40)
    title1.pack(ipady=10)

    main1 = tk.Label(
        text = "As a reaction to a trigger, such as an allergy, anaphylaxis is severe.",
        fg="white",
        bg="black",
        font=Font_tuple1, 
        justify="left")
    main1.pack()

    #Symptoms
    subheading1 = tk.Label(
        text = "Symptoms",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading1.pack()

    main2 = tk.Label(
        text = "Some of the common symptoms are: \n- Breathing difficulties, \n- Feeling lightheaded or faint, \n- Fast heartbeat, \n- Collapsing or losing consciousness. \n- Often, anaphylaxis gets progressively worse.",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left")
    main2.pack()

    photo1 = tk.PhotoImage(file = "anaphylaxis_image.png")
    image_label = tk.Label(window, image = photo1)
    image_label.pack(ipady=10)

    main5 = tk.Label(
        text="Image taken from: www.medicalnewstoday.com",
        fg = "white",
        bg="black",
        highlightthickness=4,
        highlightbackground="gray",
        width=35)
    main5.pack()

    #Steps
    subheading2 = tk.Label(
        text = "Steps to carry out when someone has anaphylaxis",
        fg = "white",
        bg="black",
        font = Font_tuple,
        justify="left")
    subheading2.pack(ipady=10)

    main3 = tk.Label(
        text = "1. Use an adrenaline auto-injector; \n2. Call 999 for an ambulance immediately; \n3. Remove any possible triggers; \n4.Lie the person down and raise their legs; \n5. Give another injection after 5 minutes.",
        fg = "white",
        bg="black",
        font=Font_tuple1,
        justify="left",
        highlightthickness=1,
        highlightbackground="gray",
        width=35)
    main3.pack()

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
