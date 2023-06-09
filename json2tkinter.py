# Name: Mohammed Alsayegh

from pathlib import Path
from PIL import Image, ImageTk

from tkinter import *
from tkinter import ttk
import json

class App:
    def __init__(self, master=Tk()):
        self.master = master
        master.resizable(False, False)

        screen_width = master.winfo_screenwidth()  # Width of the screen
        screen_height = master.winfo_screenheight() # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        width = 720
        height = 450
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)

        master.geometry('%dx%d+%d+%d' % (width, height, x, y))
        master.configure(bg = "#B2B99F")
        master.resizable(False, False)

        # Create A Main frame
        self.main_frame = Frame(master)
        self.main_frame.pack(fill=BOTH,expand=1)

        # Create Frame for X Scrollbar
        self.sec = Frame(self.main_frame)
        self.sec.pack(fill=X,side=BOTTOM)

        # Create A Canvas
        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        # Add A Scrollbars to Canvas
        self.y_scrollbar = ttk.Scrollbar(self.main_frame,orient=VERTICAL,command=self.my_canvas.yview)
        self.y_scrollbar.pack(side=RIGHT,fill=Y)

        # Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.my_canvas.bind("<Configure>",lambda e: self.my_canvas.config(scrollregion= self.my_canvas.bbox(ALL))) 

        # Create Another Frame INSIDE the Canvas
        self.second_frame = Frame(self.my_canvas)

        # Add that New Frame a Window In The Canvas
        self.my_canvas.create_window((0,0),window= self.second_frame, anchor="nw")

        file = open("example4.json","r")
        example = file.read()
        file.close()
        self.json_field = json.loads(example)
        self.create_json_widget()

    def button_creation(self,widget_counter):
        return Button(self.second_frame ,text=f"Button {widget_counter}")

    def label_creation(self,widget_counter):
        return Label(self.second_frame, text="Label Hello from Json", font=("Helvetica", 14))

    def entery_creation(self,widget_counter):
        return Entry(self.second_frame)

    def create_json_widget(self):
        list_range=len(self.json_field)
        key_json_field=list(self.json_field.keys())
        value_json_field=list(self.json_field.values())
        print(list_range)
        print(key_json_field)
        self.widget_list=[]

        dict_widget ={
            "Entry":self.entery_creation,
            "Button":self.button_creation,
            "Label": self.label_creation
        }

        count=0
        for widget_counter in range(list_range):
            # create lebal with key name
            b=Label(self.second_frame, text=key_json_field[widget_counter], font=("Helvetica", 14)) 
            b.grid(row=count,column=0,pady=5,padx=220,ipadx=100,ipady=20)
            self.widget_list.append(b)

            # create widget based on value name
            b = dict_widget[value_json_field[widget_counter]](widget_counter)
            b.grid(row=count+1,column=0,pady=10,padx=220,ipadx=100,ipady=20)
            count=count+2
            self.widget_list.append(b)

    def close(self, *args):
        print('GUI closed...')
        self.master.quit()
        self.is_active = False

    def is_closed(self):
        return not self.is_active

    def mainloop(self):
        self.master.mainloop()
        print('mainloop closed...')

if __name__ == '__main__':
    import time
    app = App()
    app.mainloop()