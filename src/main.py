#in src package
from src import ScannerWorker

#for main command line args
import sys

def main():


    #parse number of user command line arguments
    numArguments = len(sys.argv)
    #determine if they have their own file, or if they want to run our test functionality
    if numArguments == 1:
        workerClass = ScannerWorker.ScannerWorker('../data/txt1.png')
    elif numArguments == 2:
        workerClass = ScannerWorker.ScannerWorker(sys.argv[1])
    else:
        print("please invoke the program with 0 or 1 arguments")
        
    #MAIN logic
    while(1):
        print("Hello user. Thank you for using (beta) openHighlightCopyPaste. Not all functionality is avalible. Please choose your options below: ")
        print("1) Basic OCR\n2) Generate Boundary boxes")
        
        choice = input("Enter choice: ")
        choice = int(choice)
        if choice == 1:
            print(workerClass.basicOCR())
        elif choice == 2:
            print(workerClass.genBoundaryBoxes())
        else:
            print("please choose one of the options above.")


if __name__ == '__main__':
    main()