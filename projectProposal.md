![Slide](https://github.com/bee-mcc/openHighlightCopyPaste/blob/main/openHighlightCopyPaste%20Whiteboard.jpg?raw=true)


# openHighlightCopyPaste
Input a PDF or image file containing text and highlighting, receive a .txt file containing only the highlighted text. Think OCR but higher specificity.

## Project Abstract
Despite an increasingly digitized environment, users often work with scanned documents which may or may not come with text indexed using OCR. Moreover, it is often useful to extract just a portion of text from a document. Think, for instance, of how often one uses the copy+paste functionality. Users may be making a vocabulary list, inputting text into another piece of software, sending small chunks of text, or just saving text for posterity. However, this functionality is often unavailable with many PDFs and images containing text. There are not any open solutions to implement this functionality in scanned PDF files or images with _hand drawn highlighting_ - until now. openHighlightCopyPaste will be the _de facto_ project for those looking to parse their own scanned documents, or for those looking to implement this functionality into their software easily!

![Use Case Image](https://github.com/bee-mcc/openHighlightCopyPaste/blob/main/openHighlightCopyPasteUseCase.jpg?raw=true)

## Project Relevance
A myriad of educational goals can be achieved by implementing this project. Test driven development, UML, and object oriented design will ensure that this open source project is developed intuitively and can be read _after it is written, by any developer_. This will serve to increase usability. Furthermore, this project will require teamwork, as it is a medium difficulty problem. This use of teamwork will of course necessitate source control - another practice opportunity. Moreover, a simple GUI should be written to enable non-technical users to use this project, while an API should be developed to enable developers to use our code. This will let the developers practice writing a GUI and API, as well as simple UI and UX principles. Finally, multi-threading could be used to enable this software to work in real time - generating a text file _as_ the user draws contours for the software to follow.

## Conceptual Design
Developers will design software to take a PDF file or image containing text and highlighting as a parameter. Using image contouring and OCR libraries in python, the program will return a text file containing only the highlighted portion. Functionality for end users will be provided, as well as an API to utilize our code in any other project. 



## Background

<https://github.com/bee-mcc/openHighlightCopyPaste>

**Building**


**Running**


## Required Resources
- Python
- openCV Python library
  - Image contouring
  - Image manipulation libraries
- OCR Python library like pytesseract

### Helpful open source projects
_We can add to this or use as helpful guide in making our own software from scratch_
<https://github.com/jorisschellekens/borb>
