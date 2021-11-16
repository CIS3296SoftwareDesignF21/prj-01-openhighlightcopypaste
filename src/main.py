#in src package
import ScannerWorker

#for main command line args
import sys
import IMG

def main():

    #parse number of user command line arguments
    numArguments = len(sys.argv)
    #determine if they have their own file, or if they want to run our test functionality
    if numArguments == 1:
        image = IMG.IMG('../data/txt3.png')
        workerClass = ScannerWorker.ScannerWorker(image)
    elif numArguments == 2:
        image = IMG.IMG(sys.argv[1])
        workerClass = ScannerWorker.ScannerWorker(image)
    else:
        print("please invoke the program with 0 or 1 arguments")
        
    #MAIN logic
    while(1):
        print("Hello user. Thank you for using openHighlightCopyPaste. To use this program the highlight in your image must be yellow. Please choose your options below: ")
        print("1) Basic OCR\n2) Generate Boundary boxes\n3) Get highlighted words in an output text file!\n4) Exit")
        
        choice = input("Enter choice: ")
        choice = int(choice)
        if choice == 1:
            print(workerClass.basicOCR())
        elif choice == 2:
            print(workerClass.genBoundaryBoxes())
        elif choice == 3:
            file = input("Enter name for output file (including .txt extension): ")
            file = str(file)
            f = open(file, 'a')
            workerClass.genWordBox()
            workerClass.getOutput()
            for i in image.getTextList():
                f.write(i + "\n")
            f.close()
        elif choice == 4:
            exit()
        else:
            print("please choose one of the options above.")


if __name__ == '__main__':
    main()