import tkinter as tk
import random


class Application(tk.Frame):
    
    
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800) 
        self.master = master
        self.pack()
        self.create_widgets()
        self.count = 0
        self.nots = []

        # mutli-player. randomly choose abcd and input and each number correlates with a color
        # selection = random.choice([self.change_color1, self.change_color2, self.change_color3, self.change_color4])
        # selection = self.choose_button()
        # selection()
        # self.nots.append(selection)

        self.choose_button()
  
        

    def create_widgets(self):
        self.button1 = tk.Button(self, text='ONE', command = lambda: self.change_color(button_num=1,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button1.place(anchor='center', x = 400, y = 50)

        self.button2 = tk.Button(self, text='TWO', command = lambda: self.change_color(button_num=2,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button2.place(anchor='center', x = 60, y = 390)

        self.button3 = tk.Button(self, text='THREE', command = lambda: self.change_color(button_num=2,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button3.place(anchor='center', x = 740, y = 390)

        self.button4 = tk.Button(self, text='FOUR', command = lambda: self.change_color(button_num=2,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button4.place(anchor='center', x = 400, y = 750)

    def change_color(self, button_num, num=0):
        if num == 0:
            color_name = 'red'
        elif self.button1['highlightbackground'] == 'red':
            self.count = self.count + 1
            print(self.count)

            self.choose_button()
            
            color_name = 'black'
        else:
            color_name = 'black'

        if button_num == 1:
            button = self.button1
        elif button_num == 2:
            button = self.button2
        elif button_num == 3:
            button = self.button3
        else:
            button = self.button4

        print(color_name, button)
        self.button1.configure(highlightbackground=color_name)



    def change_color1(self, num=0):
        if num == 0:
            color_name = 'red'
        elif self.button1['highlightbackground'] == 'red':
            self.count = self.count + 1
            print(self.count)
            color_name = 'black'
        else:
            color_name = 'black'
        self.button1.configure(highlightbackground=color_name)


    def change_color1(self, num=0):
        print(self.button1['highlightbackground'] == 'red')
        if num == 0:
            color_name = 'red'
        elif self.button1['highlightbackground'] == 'red':
            self.count = self.count + 1
            print(self.count)
            self.choose_button()
            color_name = 'black'
        else:
            color_name = 'black'
        self.button1.configure(highlightbackground=color_name)
       

    def change_color2(self, num=0):
        print(self.button1['highlightbackground'] == 'red')
        if num == 0:
            color_name = 'red'
        elif self.button1['highlightbackground'] == 'red':
            self.count = self.count + 1
            print(self.count)
            self.choose_button()
            color_name = 'black'
        else:
            color_name = 'black'
        self.button2.configure(highlightbackground=color_name)
       

    def change_color3(self, num=0):
        print(self.button1['highlightbackground'] == 'red')
        if num == 0:
            color_name = 'red'
        elif self.button1['highlightbackground'] == 'red':
            self.count = self.count + 1
            print(self.count)
            self.choose_button()
            color_name = 'black'
        else:
            color_name = 'black'
        self.button3.configure(highlightbackground=color_name)
        

    def change_color4(self, num=0):
        print(self.button1['highlightbackground'] == 'red')
        if num == 0:
            color_name = 'red'
        elif self.button1['highlightbackground'] == 'red':
            self.count = self.count + 1
            print(self.count)
            self.choose_button()
            color_name = 'black'
        else:
            color_name = 'black'
        self.button4.configure(highlightbackground=color_name)

    def choose_button(self, nots= []):
        if self.count == 4:
            self.end_message = tk.Label(self, text="The end!")
            self.end_message.place(anchor= "center", x = 350, y = 350)
            
        functions = [1, 2, 3, 4]
        if nots != []:
            for i in nots:
                functions.remove(i)
            print(functions)

        selection = random.choice(functions)
        self.nots.append(selection)
        self.change_color(button_num = selection, num = 0)

'''
    def choose_button(self, nots= []):
        if self.count == 4:
            self.end_message = tk.Label(self, text="The end!")
            self.end_message.place(anchor= "center", x = 350, y = 350)
            
        functions = [self.change_color1, self.change_color2, self.change_color3, self.change_color4]
        if nots != []:
            for i in nots:
                index = nots.indexOf(i)
                functions.splice(index,1)
            print(len(functions))
        selection = random.choice(functions)
        self.nots.append(selection)
        selection()
'''

   
        
        
        
        

        

root = tk.Tk()
root.geometry('800x800')
root.resizable(0,0)
app = Application(master=root)
app.mainloop()
                            
