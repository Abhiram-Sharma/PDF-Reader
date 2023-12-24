import PyPDF2

file = open('G:\Codes\general projects\PDF-Reader\sample.pdf', 'rb')
reader = PyPDF2.PdfReader(file)
l=int(len(reader.pages))
for i in range(l):
    page = reader.pages[i]
    print(page.extract_text())
 
# closing the pdf file object
file.close()