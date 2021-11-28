try:
    from PIL import Image  # PIL is the pillow
except ImportError:
    import Image

import pytesseract
from pytesseract import Output
import cv2
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time, os, random, string, argparse
from pathlib import Path
import numpy as np
from PIL import ImageTk, Image
import cv2
import pytesseract as tess

import ScannerWorker

# MAC CMD
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
# Windows CMD
# pytesseract.pytesseract.tesseract_cmd = 'C:'

class data(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Highlight-Paste")

        container = tk.Frame(self)
        container.grid()

        # BROWSE IMhAGE
        self.lbl_browse = tk.Label(self, text="Select Image :", font=("Arial", 10), fg="white")
        self.lbl_browse.grid(row=4, column=0, columnspan=3, padx=24, pady=10, sticky="w")

        self.path_browse = tk.Entry(self, text="", width=30)
        self.path_browse.grid(row=4, column=0, columnspan=3, padx=120, pady=10, sticky="w")
        # BUTTON to CALL IMAGE SHOW
        self.b1_browse = tk.Button(self, text="     Browse     ", bg="#ffffff", relief="flat",
                                   width=10, command=lambda: self.show_image())
        self.b1_browse.grid(row=4, column=0, padx=310, pady=10, columnspan=3, sticky="w")

        # DISPLAY IMAGE
        self.lbl_img = tk.Label(self, image="")
        self.lbl_img.grid(row=8, column=0, pady=25, padx=10, columnspan=3, sticky="nw")

        # BUTTON to CALL OCR
        self.b2_scan = tk.Button(self, text="     Process     ", bg="#ffffff", relief="flat",
                                 width=10, command=lambda: ScannerWorker.getOutput())
        # FOR OCR TEXT
        self.highlighted_text = tk.Text(self, height=25, width=38)

    def show_image(self):
        global path

        # OPEN FILE
        self.path = filedialog.askopenfilename(defaultextension="*.jpg", filetypes=(("JPG", "*.jpg"), ("PNG", "*.png")))
        self.path_browse.delete(0, tk.END)
        self.path_browse.insert(0, self.path)

        # RESIZE
        cv_img = cv2.cvtColor(cv2.imread(self.path), cv2.COLOR_BGR2RGB)
        h, w, no_channels = cv_img.shape

        H = 400
        imgScale = H / h
        newX, newY = cv_img.shape[1] * imgScale, cv_img.shape[0] * imgScale
        newimg = cv2.resize(cv_img, (int(newX), int(newY)))
        photo = ImageTk.PhotoImage(image=Image.fromarray(newimg))

        # SHOW IMAGE
        self.lbl_img.configure(image=photo)
        self.lbl_img.image = photo

        # ADD PROCESS BUTTON
        b2_scan_mid = int(newX / 2);
        self.b2_scan.grid(row=17, column=0, padx=b2_scan_mid, pady=10,
                          columnspan=3, sticky="w")
        self.highlighted_text.grid(row=8, column=2, padx=800, pady=26, columnspan=3, sticky="w")


'''
    def ocr(self):
        self.ocr_image = cv2.imread(self.path)
        # PREPROCESSING
        gray = cv2.cvtColor(self.ocr_image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        gray = cv2.medianBlur(gray, 3)

        corrected_img = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
        ch, cw, cno_channels = corrected_img.shape

        # RESIZE
        CH = 200
        cimgScale = CH / ch
        cnewX, cnewY = corrected_img.shape[1] * cimgScale, corrected_img.shape[0] * cimgScale
        cnewimg = cv2.resize(corrected_img, (int(cnewX), int(cnewY)))
        cphoto = ImageTk.PhotoImage(image=Image.fromarray(cnewimg))

        # REPLACE IMAGE with PREPROCESSED IMAGE
        self.lbl_img.configure(image=cphoto)
        self.lbl_img.image = cphoto

        # OCR & ADD to FILE
        ocrtext = tess.image_to_string(gray)
        text_file = open("Output.txt", "w")
        text_file.write('ocrtext')
        text_file.close()

        # ADD TEXT AS FINAL OUTPUT
        self.highlighted_text.insert(tk.END, ocrtext)
'''

if __name__ == "__main__":
    app = data()
    app.geometry("700x725+100+100")
    app.mainloop()
