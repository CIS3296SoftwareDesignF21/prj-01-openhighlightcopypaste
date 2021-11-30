#for GUI
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

#for file broswer
from pathlib import Path

#for image rendering within GUI
import cv2
from PIL import ImageTk, Image

#Highlight-Paste logic
import ScannerWorker
import IMG

class data(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Highlight-Paste")

        self.workerClass = None
        self.ScannerImage = None

        container = tk.Frame(self)
        container.grid()

        # BROWSE IMAGE
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
                                 width=10, command=lambda: self.performOCRandUpdateTextBox())
        # FOR OCR TEXT
        self.highlighted_text = tk.Text(self, height=25, width=38)

    def performOCRandUpdateTextBox(self):
        self.workerClass.genWordBox()
        self.workerClass.getOutput()

        outputStr = ""
        for words in self.ScannerImage.getTextList():
            outputStr += words +"\n"
        self.highlighted_text.insert(tk.END, outputStr)

    def show_image(self):
        global path

        # OPEN FILE
        self.path = filedialog.askopenfilename(defaultextension="*.jpg", filetypes=(("JPG", "*.jpg"), ("PNG", "*.png")))
        print(self.path)

        #create the scannerworker class which will perform the internal logic
        self.ScannerImage = IMG.IMG(self.path)
        self.workerClass = ScannerWorker.ScannerWorker(self.ScannerImage)

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

if __name__ == "__main__":
    app = data()
    app.geometry("700x725+100+100")
    app.mainloop()