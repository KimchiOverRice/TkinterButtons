import tkinter as tk
from random import *


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800) 
        self.master = master
        self.pack()
        self.create_widgets()
        
        # mutli-player. randomly choose abcd and input and each number correlaes with a color
        funcs = [change_color1, change_color2, change_color3, change_color4]
        
        

    def create_widgets(self):
        self.button1 = tk.Button(self, text='ONE', command = self.change_color1, highlightbackground='black', fg='white', height=5, width=10)
        self.button1.place(anchor='center', x = 400, y = 50)

        self.button2 = tk.Button(self, text='TWO', command = self.change_color2, highlightbackground='black', fg='white', height=5, width=10)
        self.button2.place(anchor='center', x = 60, y = 390)

        self.button3 = tk.Button(self, text='THREE', command = self.change_color3, highlightbackground='black', fg='white', height=5, width=10)
        self.button3.place(anchor='center', x = 740, y = 390)

        self.button4 = tk.Button(self, text='FOUR', command = self.change_color4, highlightbackground='black', fg='white', height=5, width=10)
        self.button4.place(anchor='center', x = 400, y = 750)


    def change_color1(self):
        color_name = 'red'
        self.button1.configure(highlightbackground=color_name)

    def change_color2(self):
        self.button2.configure(highlightbackground='red')

    def change_color3(self):
        self.button3.configure(highlightbackground='red')

    def change_color4(self):
        self.button4.configure(highlightbackground='red')

        

root = tk.Tk()
root.geometry('800x800')
root.resizable(0,0)
app = Application(master=root)
app.mainloop()
                            
