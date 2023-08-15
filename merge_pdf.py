from PyPDF2 import PdfWriter 
import os 

merge = PdfWriter()  #if we open definately we need to close the merge 
files = [file for file in os.listdir() if file.endswith(".pdf")]  #we created as dir to see the file endswith pdf 

for pdf in files:  #this is to e=merge all files in a single file 
    merge.append(pdf)

merge.write("merge.pdf")   #merged file name 
merge.close()
