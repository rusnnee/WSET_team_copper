import sys
import tkinter.messagebox as box
from tkinter.filedialog import asksaveasfile
if sys.version_info[0] >= 3:
    import tkinter as tk
else:
    import Tkinter as tk


class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.dict = {'Asia': ['Japan', 'China', 'Malaysia'],
                     'Europe': ['Germany', 'France', 'Switzerland']}

        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)

        self.variable_b.trace('w', self.fun2)
        self.variable_a.trace('w', self.update_options)


        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.dict.keys(), command=self.fun)
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')


        username = self.fun()
        password = self.fun2()


        self.button = tk.Button(self, text="Login", command=lambda : sample(username=username, password=password))


        self.variable_a.set('Asia')

        self.optionmenu_a.pack()
        self.optionmenu_b.pack()
        self.button.pack()
        self.pack()

    def fun(self,*args):
        return self.variable_a.get()

    def fun2(self, *args):
        return self.variable_b.get()


    def update_options(self, *args):
        countries = self.dict[self.variable_a.get()]
        self.variable_b.set(countries[0])

        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.variable_b.set(nation))


def sample(username, password):
    box.showinfo('info', 'Enter Credentials')


if __name__ == "__main__":
    root = tk.Tk()
    username = "root"
    password = "admin"
    app = App(root)
    app.mainloop()
