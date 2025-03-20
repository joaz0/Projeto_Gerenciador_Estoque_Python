import tkinter as objTK
from tkinter import ttk as objTTK

# Create window
objWindow = objTK.Tk()

# Initialise variables
arrHdr = ["Hdr1", "Hdr2"]
arrData = ["Test1", "Test2"]

# ------------ Treeview 1
fFrame1 = objTK.LabelFrame(objWindow, text="Tree 1")
treeView1 = objTTK.Treeview(columns=arrHdr, show="headings")

treeView1.grid(column=0, row=0, sticky="nsew", in_=fFrame1)
fFrame1.grid_columnconfigure(0, weight=1)
fFrame1.grid_rowconfigure(0, weight=1)

treeView1.heading(0, text="Hd1")
treeView1.heading(1, text="Hd2")

treeView1.insert("", "end", values=arrData)

fFrame1.pack()

# ------------ Treeview 2
fFrame2 = objTK.LabelFrame(objWindow, text="Tree 2")
treeView2 = objTTK.Treeview(columns=arrHdr, show="headings")

objStyle = objTTK.Style(treeView2)
objStyle.theme_use("clam")
objStyle.configure("Treeview.Heading", background="#c3c3c3")

treeView2.grid(column=0, row=0, sticky="nsew", in_=fFrame2)
fFrame2.grid_columnconfigure(0, weight=1)
fFrame2.grid_rowconfigure(0, weight=1)

treeView2.heading(0, text="Hd1")
treeView2.heading(1, text="Hd2")

treeView2.insert("", "end", values=arrData)

fFrame2.pack()

objWindow.bind("<Escape>", lambda wExit: objWindow.destroy())

objWindow.mainloop()