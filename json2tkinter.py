# Name: Mohammed Alsayegh

from pathlib import Path
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import colorchooser

class App:
    def __init__(self, master=tk.Tk()):
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
        

    def create_json_widget(self):
        list_range=len(json_field)
        key_json_field=list(json_field.keys())
        value_json_field=list(json_field.values())
        print(list_range)
        print(key_json_field)
        self.widget_list=[]

        dict_widget ={
            "Entry":"Entry(self.second_frame)",
            "Button":"""Button(self.second_frame ,text=f"Button {widget_counter}")""",
            "Label":"""Label(self.second_frame, text="Label Hello from Json", font=("Helvetica", 14))"""
        }

        for widget_counter in range(list_range):
            # create lebal with key name
            b=Label(self.second_frame, text=key_json_field[widget_counter], font=("Helvetica", 14)) 
            b.grid(row=count,column=0,pady=5,padx=220,ipadx=100,ipady=20)
            self.widget_list.append(b)

            # create widget based on value name
            my_code =  dict_widget[value_json_field[widget_counter]]
            b = eval(my_code)
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