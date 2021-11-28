# openHighlightCopyPaste

# About
OpenHighlightCopyPaste takes an image of a document as input and extracts the highlighted words. Currently, the intended users are students or anybody else that has use of the program. The user needs to be somewhat tech-savvy to be able to install the required dependencies. 

openHighlightCopyPaste was created solely with the Python language and implements the Python OpenCV and Pytesseract libraries. Pytesseract is a wrapper for Google's Tesseract-OCR Engine and is for text recognition in the program. OpenCV is used for image handling, including cleaning up the image for OCR processing and determining the highlighted words. 

# Users

## How to Install
### Installation Prerequisites

1) Follow instructions [here](https://www.python.org) to install the latest version of python, including pip
2) Follow instructions [here](https://tesseract-ocr.github.io/tessdoc/Compiling.html) to install the tesseract binary. Make sure you update your PATH variable with the path to tesseract's binary, or verify that the binary is already installed by running ```which tesseract```

### Installation
#### Option 1 - pip
1) Go to most recent [release](https://github.com/CIS3296SoftwareDesignF21/prj-01-openhighlightcopypaste/releases) and download *openHighlightCopyPaste-1.0.1-py3-none-any.whl*
2) Open directory where you downloaded the file and run the following command:
```pip install openHighlightCopyPaste-1.0.1-py3-none-any.whl ```

#### Option 2 - source code
1) Go to most recent [release](https://github.com/CIS3296SoftwareDesignF21/prj-01-openhighlightcopypaste/releases) and download zipped source code
2) Unzip and navigate to the src folder in the project.

## How to Run

*Important Note*        
Image must use yellow highlight for this program to work.
### Option 1 - installed with pip
Run the following command:       
MacOS/Linux ```python3 -m src.main path/to/image/here```    
Windows ```py -m src.main path/to/image/here ``` 

You will then be prompted to either print out the text, or to show the boundaries of the letters/words, or get an output text file with the highlighted words. Select the option you wish. 

### Option 2 - installed source code

MacOS/Linux run:
```python3 main.py path/to/image/here ```     
Windows run:
```py main.py path/to/image/here ```

You will then be prompted to either print out the text, or to show the boundaries of the letters/words, or get an output text file with the highlighted words. Select the option you wish. 


# Developers
## How to Install for Development and Testing 

### Dependencies

1) Follow instructions [here](https://www.python.org) to install the latest version of python
2) Follow instructions [here](https://tesseract-ocr.github.io/tessdoc/Compiling.html) to install the tesseract binary. Make sure you update your PATH variable with the path to tesseract's binary, or verify that the binary is already installed by running ```which tesseract```


### Our project
1) Navigate to the direction in which you'd like to install our project using the command line
2) Run ```python3 -m venv ./.venv``` to create a hidden virtual environment directory
3) Run the following command to clone the repository ```git clone https://github.com/CIS3296SoftwareDesignF21/prj-01-openhighlightcopypaste.git ```
4) Run the following command to activate the virtual enviroment ```source .venv/bin/activate```
5) Run the following command to install all python dependencies ```pip install -r requirements.txt```

## How to Run 

Run the following commands from the directory which contains .venv and the repository
```cd prj-01-openhighlightcopypaste```
```cd src```        
MacOS/Linux run:
```python3 main.py ``` OR ```python3 main.py path/to/image/here ```     
Windows run:
```py main.py ``` OR ```py main.py path/to/image/here ```

Then follow the prompts in your command line


## Development Documents

#### [UML Diagram (initial proposal)](docs/devDocs/UML/openHighlightCopyPaste.drawio.png)

#### [Project Proposal](docs/devDocs/projectProposal.md)

#### [Vision Statement and Personas](docs/devDocs/Vision_Personas.md)

### Project Contributions and Accomplishments
* [Week 1](docs/devDocs/week1.md)
* [Week 2](docs/devDocs/week2.md)
* [Week 3](doc/devDocs/week3.md)

