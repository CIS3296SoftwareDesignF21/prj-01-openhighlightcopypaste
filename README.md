# Highlight-Paste

[About](#about) | [Users](#users) | [Developers](#developers) | [Future Plans](#future-plans)


# About
Highlight-Paste takes an image of a document as input, in either .png or .jpg formats, and extracts the highlighted words. Currently, the intended users are students or anybody else that has use of the program. The user needs to be somewhat tech-savvy to be able to install the required dependencies. 

Highlight-Paste was created solely with the Python language and implements the Python OpenCV and Pytesseract libraries. Pytesseract is a wrapper for Google's Tesseract-OCR Engine and is for text recognition in the program. OpenCV is used for image handling, including cleaning up the image for OCR processing and determining the highlighted words. 


# Users

## How to Install
### Installation Prerequisites

1) Follow instructions [here](https://www.python.org) to install the latest version of python, including pip
2) Follow instructions [here](https://tesseract-ocr.github.io/tessdoc/Compiling.html) to install the tesseract binary. Make sure you update your PATH variable with the path to tesseract's binary, or verify that the binary is already installed by running ```which tesseract```

### Installation
Go to most recent [release](https://github.com/CIS3296SoftwareDesignF21/prj-01-openhighlightcopypaste/releases) and download *Highlight-Paste.exe* for Windows or *Highlight-Paste* for Mac/Unix.

## How to Run
**Prerequisites to installation MUST be completed for program to work!**  

*Running*
* Windows: Run Highlight-Paste.exe
* Mac/Unix based: Double click Highlight-Paste executable file
* Select image file (either .png or .jpg) via input form in window.
* Select process to return list of highlighted words. You can copy the returned words from the screen into your own file.

*Important steps for accurate processing:*
* Make sure document you are using has a *white* background, and you can use any highlight color you wish.
* Make sure picture has text aligned horizontally for accurate text recognition. Do not submit images with the text not aligned horizontally.

*Additional note for Winows users:*       
When running the program for the first time Microsoft Defenfer may try to block the app because it is unrecognized. Select *More info* and then select *Run anyway*. 

*Additional note for Mac users:* 
If you are unable to open the executable file for security reasons (as described above) navigate to System Preferences > Security and Privacy > General, and there should be an option along the bottom to allow this app


# Developers
## How to Install for Development and Testing 

### Installing Dependencies

1) Follow instructions [here](https://www.python.org) to install the latest version of python
2) Follow instructions [here](https://tesseract-ocr.github.io/tessdoc/Compiling.html) to install the tesseract binary. Make sure you update your PATH variable with the path to tesseract's binary, or verify that the binary is already installed by running ```which tesseract```


### Installing The Project
1) Navigate to the direction in which you'd like to install our project using the command line
2) Run one of the following to create a hidden virtual environment directory:        
   MacOS/Linux: ```python3 -m venv ./.venv```      
   Windows: ```py -m venv ./.venv```          
3) Run the following command to clone the repository ```git clone https://github.com/CIS3296SoftwareDesignF21/prj-01-openhighlightcopypaste.git ```            
4) Run one of the following commands to activate the virtual enviroment:         
   MacOS/Linux: ```source .venv/bin/activate```         
   Windows:  ```C:\<path to project>\.venv\Scripts\activate.bat```  OR enter into Scripts folder and run activate.bat          
5) Run the following command to install all python dependencies ```pip install -r requirements.txt```

## How to Run 

Run the following commands from the directory which contains .venv and the repository
```cd prj-01-openhighlightcopypaste```
```cd src```        
MacOS/Linux run:
```python3 GUImain.py ```     
Windows run:
```py GUImain.py ``` 

## Building for distribution

We use PyInstaller to build for distribution. Run:

```pyinstaller GUImain.py IMG.py ScannerWorker.py --windowed --name=Highlight-Paste --onefile```

on your given system to produce a packaged file that works for that system.

## Development Documents

#### Program Related
 [Vision Statement and Personas](docs/devDocs/Vision_Personas.md) | [Class Diagram](docs/devDocs/UML/openHighlightWeek3DemoEdits.drawio.png) | [Sequence Diagram 1](docs/devDocs/UML/SeqDiaOpt1.png) | [Sequence Diagram 2](docs/devDocs/UML/SeqDiaOpt2.png)  


#### Accomplishments
 [Weekly Accomplishments](docs/devDocs/WeeklyAccomplishments) | [Most Recent Accomplishments](docs/devDocs/WeeklyAccomplishments/week4.md) 



# Future Plans

* Package program completely to expand user base
* Distinguish different lists based on highlight color
* GUI app with realtime PDF rendering, highlighting, and text return
