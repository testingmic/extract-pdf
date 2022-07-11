import sys
import os

def fileexist(filename):
    try:
        open(filename, 'rb')
        return 1
    except FileNotFoundError:
        return 0

def main():
    try:
        from PyPDF2 import PdfReader

        argument_count = len(sys.argv)

        # check that file was parsed in the arguments list
        if(argument_count < 2):
            print("Please specify the pdf file name")
            return

        # get the file name
        filename = sys.argv[1]

        # confirm that the file exists
        if(fileexist(filename) == 0):
            print("Sorry! The file ", filename, " does not exist")
            return

        # check the file extension
        split_up = os.path.splitext(filename)

        # confirm pdf extension
        if(split_up[1] != '.pdf'):
            print("Sorry! A pdf document was expected.")
            return

        # create object of the module
        reader = PdfReader(filename)
        number_of_pages = len(reader.pages)
        print("This document has ", number_of_pages, "number of pages\n")

        # loop through the document pages
        for x in range(0, number_of_pages):
            print("Reading from Page: ", x, "\n")
            page = reader.pages[x]
            text = page.extract_text()
            pdf_text = text.encode('utf-8', errors='ignore')
            print(pdf_text)
            print("\n")

    except ImportError:
        print("Execution Failed. The Module PyPDF2 could not be found")

if __name__ == "__main__":
    main()
