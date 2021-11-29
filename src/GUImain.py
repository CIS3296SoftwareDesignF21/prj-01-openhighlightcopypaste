#for GUI
import tkinter as tk
from tkinter import *

#for file broswer
from pathlib import Path

#for image rendering within GUI
import cv2
from PIL import ImageTk, Image

#Highlight-Paste logic
import ScannerWorker
import IMG

if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Highlight-Paste")
    gui.geometry("700x725+100+100")

    #create the header (a lable object with gui as its root)
    header = Label(gui, text = "Welcome to Highlight-Paste!", font=("Arial", 45))
    #position the header (by using the grid function, which places the object at its parameters)
    header.grid(column = 0, row= 0, columnspan=3, rowspan=3)

    fileWindow = Frame(gui, background="grey")
    fileWindow.grid(column=0, row=3, columnspan=3, rowspan= 4)

    fileWindowContents = Button(fileWindow, text="Browse for Image", width=10)



    #start the GUI (ie display elements)
    gui.mainloop()