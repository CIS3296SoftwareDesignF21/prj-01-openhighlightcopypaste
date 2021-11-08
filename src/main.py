#in src package
import ScannerWorker
#for main command line args
import sys

def main():

    #initialize worker class
    workerClass = ScannerWorker.ScannerWorker()

    #parse number of user command line arguments
    numArguments = len(sys.argv)
    #determine if they have their own file, or if they want to run our test functionality
    if numArguments == 1:
        workerClass.test('../data/txt1.png')
    elif numArguments == 2:
        workerClass.test(sys.argv[1])
    else:
        print("please invoke the program with 0 or 1 arguments")
        


if __name__ == '__main__':
    main()