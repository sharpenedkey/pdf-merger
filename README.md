A small Python script that merges all PDF files in a specific directory into one by appending them one after the other.

Usage guide:
1. Place the script into the same directory as the files to be merged
2. Make sure the files are numbered in ascending order and named the way you would want the corresponding bookmarks to be named. For example, a file named "2 - CV.pdf" that comes up second in the list would be the second chapter of the resulting PDF file, with a bookmark called "CV" pointing to its beginning.
3. Run the pdf_merger.py file by double-clicking it
4. After the script is finished, the resulting file can be found in a sub-directory called "Done"

Notes: 
- if the original files have their own bookmarks, they will not be transferred to the new file!
- if some or all files are not numbered, then they will be merged in alphabetic order
- if the final file "result.pdf" already exists, it gets overwritten after the script is run again

test github push