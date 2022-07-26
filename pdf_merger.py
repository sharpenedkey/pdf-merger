from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import os


def pdf_merger():
    
    """
    Merges all PDF files in the current directory into one PDF file.
    """

    # Scans all of the pdf files in the current directory
    # and creates a list with all of their names
    path = os.getcwd()
    pdfs = []
    for entry in os.scandir(path):
        if (entry.name.endswith(".pdf")):
            pdfs.append(entry.name)

    # Merges all of the files from the above list and
    # also creates a list where the page numbers are listed (i.e.
    # on which page each new file in the merged pdf will appear)
    pages = []
    file_start = 0
    merger = PdfFileMerger(strict=False)
    for pdf in pdfs:
        merger.append(pdf, import_bookmarks=False)
        cur_file = PdfFileReader(pdf, strict=False)
        pages.append(file_start)
        file_start += cur_file.getNumPages()
        print("Merged file \"" + pdf + "\"")
    print()

    # Writes the (temporary) merged pdf file in a folder called
    # "Done", which is created if it doesn't exist
    path_done = os.path.join(path, "Done")
    if not os.path.isdir(path_done):
        os.makedirs(path_done)
    path_merged_pdf = os.path.join(path_done, "merged.pdf")
    merger.write(path_merged_pdf)

    # Initializes the file writer and the file reader
    # for the final pdf file
    writer = PdfFileWriter()
    reader = PdfFileReader(path_merged_pdf)

    # Re-creates merged.pdf using the file writer in order
    # to then create actually working bookmarks (apparently
    # FileMerger can't do it well enough)
    input_numpages = reader.getNumPages()
    for i in range(input_numpages):
        writer.addPage(reader.getPage(i))

    # Creates the bookmarks named just like the original pdf
    # files' names
    for pdf in pdfs:
        name_without_number = str.strip(pdf, "1234567890 -")
        name_without_pdf = str.rstrip(name_without_number[:-4])
        writer.addBookmark(name_without_pdf, pages[pdfs.index(pdf)], parent=None)
        print("Created bookmark \"" + name_without_pdf + "\"")
    print()
    writer.setPageMode("/UseOutlines")

    # Writes the newly re-created (now final) merged.pdf file
    with open(path_merged_pdf, "wb") as fp:
        writer.write(fp)

    # Prints the final output
    print("Finished!")
    print("The final file is located at: " + path_merged_pdf + "\n")
    input("Press ENTER to exit")


pdf_merger()