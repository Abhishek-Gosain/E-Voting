from tkinter import *
import sqlite3
import cv2
import os
import numpy as np
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
from PIL import Image


root=Tk()

def showimage():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
    img=Image.open(fln)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)
    lbl.configure(image = img)
    lbl.image=img
   

frm=Frame(root)
frm.pack(side=BOTTOM,padx=15,pady=15)
 
lbl=Label(root)
lbl.pack()

btn=Button(frm,text="Browse Image",command=showimage)
btn.pack(side=tk.LEFT)

btn2=Button(frm,text="Exit",command=lambda: exit())
btn2.pack(side=tk.LEFT,padx=10)

root.title("Image Browser")
root.geometry("300x350")
root.mainloop()

    


