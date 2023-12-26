import PyPDF2
from autocorrect import Speller
file = open('G:\Codes\general projects\PDF-Reader\sample.pdf', 'rb')
reader = PyPDF2.PdfReader(file)
l=int(len(reader.pages))
a=[]
c=''
d=[]
n=Speller(lang='en')
for i in range(l):
    page = reader.pages[i]            
    x=page.extract_text()                    #Extracting the file
    a.append(x)                              #Adding to the list
for b in a:
    l=b.replace('\n',' ')                    #removing spaces in the text
    e=l.split()                              #spliting the text into words
    d.append(e)                              #Adding to the list
for z in d:
    for f in z:
        print(n(f))                          #Printing the correct words
                                            
file.close()                                 # closing the pdf file object
