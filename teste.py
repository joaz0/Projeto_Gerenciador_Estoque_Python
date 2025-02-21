import os, sys
from tkinter import *
import tkinter

root = tk.Tk()

def input_count():
    try:
        user_submission=int(user_text.get())
    except:
        wrong_submission=tk.Label(frame_top,  text="That isn't a number, try again!", justify = tk.LEFT, padx = 20)
        wrong_submission.grid(column=0 , row=1)
    else:
        try:
            frame_bottom.grid_forget()
        except:
            pass
        frame_bottom = tk.Frame(root)
        frame_bottom.grid(row = 2, column = 0, sticky = "nsew")
        for num in range(0,user_submission):
            old_row=2
            new_row=old_row+(2*num)
            extra_new_row= new_row + 1
            animal_check=tk.Label(frame_bottom, text='Enter an animal', justify = tk.LEFT, padx = 20)
            animal_check.grid(column=0, row=new_row)
            animal_text = tk.Entry(frame_bottom, width= 50)
            animal_text.grid(column=1, row=new_row)
            colour_check=tk.Label(frame_bottom,  text='Enter a colour', justify = tk.LEFT, padx = 20)
            colour_check.grid(column=0, row=extra_new_row)
            colour_text = tk.Entry(frame_bottom, width= 50)
            colour_text.grid(column=1, row=extra_new_row)

frame_top = tk.Frame(root)
frame_top.grid(row = 0, column = 0, sticky = "nsew")

frame_bottom = tk.Frame(root)
frame_bottom.grid(row = 2, column = 0, sticky = "nsew")

user_label=tk.Label(frame_top, text='Enter a number', justify = tk.LEFT, padx = 20)
user_label.grid(column=0 , row=0)
user_text= tk.Entry(frame_top, width= 50)
user_text.grid(column=1, row=0)
user_submit=tk.Button(frame_top,text="SUBMIT", command=input_count)
user_submit.grid(column=2,row=0)

root.mainloop()