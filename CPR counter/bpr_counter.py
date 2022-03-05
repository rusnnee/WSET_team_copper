from tkinter import *
import time

root = Tk()

#variable is stored in the root object
root.counter = 0
times = []
def clicked():
    times.append(time.time())      
    root.counter += 1

    if root.counter == 1:
        freq = 0
    else:
        dt = times[root.counter - 1] - times[root.counter - 2]
        freq = int ((1/dt) *60)
    
    L['text'] = 'Button clicked: ' + str(root.counter)
    L1['text'] = 'Freq: ' + str(freq)
        
b = Button(root, text="Click Me", command=clicked)
b.pack()

L = Label(root, text="No clicks yet.")
L.pack()

L1 = Label(root, text="No clicks yet.")
L1.pack()

root.mainloop()
