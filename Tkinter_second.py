import tkinter as tk
import random
import time, threading

# TO DO:
# Make a start button
# Make a timer
# Declare the winner at the end


'''
* This class is for the frame of the tkinter window
* It inherits the tk.Frame class made in the Tkinter library
'''
class Application(tk.Frame):

    '''
    * Contructor intializes the frame, creates buttons, allows keyboard clicks
    * and chooses a random button to light up first
    '''
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800) 
        self.master = master
        self.pack()

        #create buttons
        self.create_widgets()

        # listen for keys pressed and call function key_press()
        self.master.bind('<Key>', self.key_press)

        #initialize empty list that will keep track of each player's presses
        self.count = [0] * 3

        # choose buttons to light up different colors
        self.begin()
        
  
    '''
    * This function creates the buttons and places them
    '''
    def create_widgets(self):

        # declare and initialize, label, and place buttons, also added functions
        self.button1 = tk.Button(self, text='ONE', command = lambda: self.change_color(button_num=1,color_num=0), highlightbackground='black', fg='white', height=5, width=10)
        self.button1.place(anchor='center', x = 400, y = 50)

        self.button2 = tk.Button(self, text='TWO', command = lambda: self.change_color(button_num=2,color_num=0), highlightbackground='black', fg='white', height=5, width=10)
        self.button2.place(anchor='center', x = 60, y = 390)

        self.button3 = tk.Button(self, text='THREE', command = lambda: self.change_color(button_num=3,color_num=0), highlightbackground='black', fg='white', height=5, width=10)
        self.button3.place(anchor='center', x = 740, y = 390)

        self.button4 = tk.Button(self, text='FOUR', command = lambda: self.change_color(button_num=4,color_num=0), highlightbackground='black', fg='white', height=5, width=10)
        self.button4.place(anchor='center', x = 400, y = 750)

        # make button list
        self.buttons = [self.button1, self.button2, self.button3, self.button4]


    '''
    * This function randomly chooses the next button to light up. If
    * the count is 4, this funciton will send out an ending message.
    * This function ensures the same button will not be chosen twice.
    '''

    def begin(self):
            
        button_list = [1, 2, 3, 4]
        nots = []

        for i in range(3):
            for j in button_list:
                if j in nots:
                    button_list.remove(j)

            selection = random.choice(button_list)

            nots.append(selection)
            print("interation:", i, "  button selection:", selection)
            self.change_color(button_num=selection, color_num=i+1)

    '''
    * This function changes the color of the button designated by button_num
    * to the color designated by num. If the button designated was originally red,
    * this function chooses calls choose_button, to light up the next button
    '''
    def change_color(self, button_num, color_num=0):

        colors = ['black', 'red', 'green', 'blue']
        the_button = self.buttons[button_num - 1]

        # check if you need to change color
        if the_button['highlightbackground'] in colors[1:4]:
            print("Is the background in colors 1-4:", the_button['highlightbackground'] in colors[1:4])

            # get the old color to put into choose button
            for i in colors:
                if the_button['highlightbackground'] == i:
                    color_id = colors.index(i)
                    
            # increase the count
            print("color_id:", color_id)
            self.count[color_id-1] = self.count[color_id-1] + 1

            print("count: ", self.count)
            the_button.configure(highlightbackground = colors[color_num])
            self.choose_button(button_num, color_id)

        else:
            # color change when original color is black. this will be used by begin()
            # or when a black button is accidentally pressed
            the_button.configure(highlightbackground = colors[color_num])
 


    def choose_button(self, old, color_number):

        if any(i >= 4 for i in self.count):
            winner = self.count.index(4)
            self.end(winner)
            return
        
        print("after the end check") 
        free_buttons = self.get_free_buttons()
        print("free buttons in choose_button:", free_buttons, "\nold:", old)
        
        if old in free_buttons:
            free_buttons.remove(old)
        print("free buttons after removal:", free_buttons)

        selection = random.choice(free_buttons)
     

        print("selection:", selection," color_num:", color_number)
        self.change_color(button_num=selection, color_num=color_number)

    '''
    * This function returns the buttons that are not currently lit up
    '''
    def get_free_buttons(self):
        free_buttons = []
        for i in range(4):
            button = self.buttons[i]
            if button['highlightbackground'] == 'black':
                free_buttons.append(i + 1)
        return free_buttons
                

    '''
    * This links the color_change function to keyboard buttons. 
    '''
    def key_press(self, event):
        key = event.char
        if key.isnumeric():
            key = int(key)
        print(key, 'is pressed')
        if key in range(1, 5):
            self.change_color(button_num=key,color_num=0)

    def end(self, color_index):
        colors = ['black', 'red', 'green', 'blue']
        
        winners_message = "The " + colors[color_index+1] + " player won!"

        self.end_message0 = tk.Label(self, text="CONGRATULATIONS!", font=("Courier", 40))
        self.end_message0.place(anchor= "center", x = 400, y = 350)
        
        self.end_message1 = tk.Label(self, text=winners_message, font=("Courier", 20))
        self.end_message1.place(anchor= "center", x = 400, y = 400)


        
        

        

root = tk.Tk()
root.geometry('800x800')
root.title("Four Buttons")
root.resizable(0,0)
app = Application(master=root)
app.mainloop()
                  
