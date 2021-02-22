import tkinter as tk
import random

# TO DO:
# Write better comments

class Application(tk.Frame):
    
    
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800) 
        self.master = master
        self.pack()
        self.create_widgets()

        self.master.bind('<Key>', self.key_press)
        
        self.count = 0
        self.last_selection = 100

        # mutli-player. randomly choose abcd and input and each number correlates with a color

        self.choose_button()
        
  
        

    def create_widgets(self):
        self.button1 = tk.Button(self, text='ONE', command = lambda: self.change_color(button_num=1,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button1.place(anchor='center', x = 400, y = 50)

        self.button2 = tk.Button(self, text='TWO', command = lambda: self.change_color(button_num=2,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button2.place(anchor='center', x = 60, y = 390)

        self.button3 = tk.Button(self, text='THREE', command = lambda: self.change_color(button_num=3,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button3.place(anchor='center', x = 740, y = 390)

        self.button4 = tk.Button(self, text='FOUR', command = lambda: self.change_color(button_num=4,num=1), highlightbackground='black', fg='white', height=5, width=10)
        self.button4.place(anchor='center', x = 400, y = 750)

    def change_color(self, button_num, num=0):

        if button_num == 1:
            button = self.button1
        elif button_num == 2:
            button = self.button2
        elif button_num == 3:
            button = self.button3
        else:
            button = self.button4

        # print("Was it the button red:", button['highlightbackground'] == 'red')
        if num == 0:
            color_name = 'red'
        
        elif button['highlightbackground'] == 'red':
            self.count = self.count + 1

            print("count: ", self.count)

            self.choose_button()

            color_name = 'black'
        else:
            color_name = 'black'


        # print("Changed to", color_name, " Button:", button)
        button.configure(highlightbackground = color_name)



    def choose_button(self, nots= []):
        if self.count >= 4:
            self.end_message = tk.Label(self, text="The end!", font=("Courier", 44))
            self.end_message.place(anchor= "center", x = 400, y = 400)
            return
            
        functions = [1, 2, 3, 4]
        # print("last selection:", self.last_selection)
        if self.last_selection != 100:
            functions.remove(self.last_selection)
        # print("functions list:", functions)
        selection = random.choice(functions)
        # print("selection:", selection)
        self.last_selection = selection
        self.change_color(button_num = selection, num = 0)

    def key_press(self, event):
        key = event.char
        if key.isnumeric():
            key = int(key)
        print(key, 'is pressed')
        self.change_color(button_num=key,num=1)
        

        

root = tk.Tk()
root.geometry('800x800')
root.title("Four Buttons")
root.resizable(0,0)
app = Application(master=root)
app.mainloop()
                            
