#for GUI
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
    gui = Tk()
    gui.title("Highlight-Paste")
    gui.geometry("700x925")
    
    gui.mainloop()